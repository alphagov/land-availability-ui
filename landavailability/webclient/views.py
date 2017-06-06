from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import messages

import requests

log = __import__('logging').getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "index.html"


class SearchView(TemplateView):
    template_name = "results.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        postcode = request.GET.get('location')
        center_distance = request.GET.get('center_distance')
        polygon = request.GET.get('polygon')

        if center_distance:
            # Miles to Meters conversion
            range_distance = float(center_distance) * 1609.34
        else:
            # Set a default value
            range_distance = 1000

        headers = {
            'Authorization': 'Token {0}'.format(
                settings.LAND_AVAILABILITY_API_TOKEN)}
        url = '{0}/api/locations/'.format(
            settings.LAND_AVAILABILITY_API_URL)
        generic_error_msg = 'There was a problem. The admins have been ' \
            'notified. Please try again later.'

        try:
            if polygon:
                response = requests.get(
                    url,
                    params={'polygon': polygon},
                    headers=headers)
            else:
                response = requests.get(
                    url,
                    params={
                        'postcode': postcode,
                        'range_distance': range_distance},
                    headers=headers)

        except Exception as ex:
            log.error('Problem connecting to url %s: %s',
                      url, ex)
            messages.add_message(request, messages.ERROR,
                                 generic_error_msg)

        if response.status_code == requests.codes.ok:
            try:
                context['results'] = response.json()
            except ValueError:
                log.error('Non-json response from %s: %s',
                          response.url, response.text)
                messages.add_message(request, messages.ERROR,
                                     generic_error_msg)
            context['terms'] = request.GET
        else:
            log.error('Bad status querying url %s: %s',
                      response.url, response.text)
            messages.add_message(request, messages.ERROR, generic_error_msg)

        # TODO Get 'count' out of the API
        return self.render_to_response(context)


class LocationDetailsView(TemplateView):
    template_name = "location.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        uprn = kwargs.get('uprn')

        try:
            headers = {
                'Authorization': 'Token {0}'.format(
                    settings.LAND_AVAILABILITY_API_TOKEN)}
            url = '{0}/api/locations/{1}/'.format(
                settings.LAND_AVAILABILITY_API_URL,
                uprn)
            response = requests.get(url, headers=headers)
            context['location'] = response.json()
        except Exception as ex:
            # Log error here
            pass
        return self.render_to_response(context)
