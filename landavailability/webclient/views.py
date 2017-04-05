from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import requests


class HomePageView(TemplateView):
    template_name = "index.html"


class SearchView(TemplateView):
    template_name = "results.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        postcode = request.GET.get('location')
        center_distance = request.GET.get('center_distance')

        if center_distance:
            # Miles to Meters conversion
            range_distance = float(center_distance) * 1609.34
        else:
            # Set a default value
            range_distance = 1000

        try:
            headers = {
                'Authorization': 'Token {0}'.format(
                    settings.LAND_AVAILABILITY_API_TOKEN)}
            url = '{0}/api/locations/'.format(
                settings.LAND_AVAILABILITY_API_URL)
            response = requests.get(
                url,
                params={
                    'postcode': postcode,
                    'range_distance': range_distance},
                headers=headers)
            context['results'] = response.json()
            context['terms'] = request.GET
        except Exception as ex:
            # Log error here
            pass
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
