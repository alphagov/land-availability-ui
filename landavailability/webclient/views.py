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

        try:
            headers = {
                'Authorization': 'Token {0}'.format(
                    settings.LAND_AVAILABILITY_API_TOKEN)}
            url = '{0}/api/location/'.format(
                settings.LAND_AVAILABILITY_API_URL)
            response = requests.get(
                url,
                params={
                    'postcode': request.GET.get('location'),
                    'range_distance': 1000},
                headers=headers)
            context['results'] = response.json()
            context['terms'] = request.GET
        except Exception as ex:
            # Log error here
            pass
        return self.render_to_response(context)
