from unittest import TestCase
from django.test import override_settings
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
import pytest
import responses
import json


class WebclientViewTestCase(TestCase):
    @override_settings(STATICFILES_STORAGE=None)
    def test_index_can_be_loaded(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Sign in' in str(response.content))

    @pytest.mark.django_db
    @override_settings(STATICFILES_STORAGE=None)
    def test_index_has_signout_when_logged(self):
        client = Client()
        User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword')
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Sign out' in str(response.content))

    @pytest.mark.django_db
    @override_settings(STATICFILES_STORAGE=None)
    @responses.activate
    def test_search_view_postcode(self):
        client = Client()
        url = reverse('search')

        json_body = [{
            'nearest_school_distance': None,
            'nearest_metrotube_distance': None,
            'geom': {
                'coordinates': [
                    [
                        [
                            [
                                0.13153553009033203,
                                52.205765731674575
                            ],
                            [
                                0.13143360614776609,
                                52.20569340742784
                            ],
                            [
                                0.13174474239349365,
                                52.20561122064091
                            ],
                            [
                                0.13180643320083618,
                                52.20569669489615
                            ],
                            [
                                0.13153553009033203,
                                52.205765731674575
                            ]
                        ]
                    ]
                ],
                'type': 'MultiPolygon'
            },
            'authority': 'Cambridge City Council',
            'uprn': '010090969147',
            'nearest_broadband': None,
            'nearest_ohl_distance': None,
            'nearest_trainstop': None,
            'nearest_trainstop_distance': None,
            'unique_asset_id': None,
            'name': 'Allia Ltd',
            'owner': '',
            'id': 38,
            'nearest_school': None,
            'nearest_broadband_distance': None,
            'nearest_greenbelt': None,
            'nearest_busstop_distance': None,
            'ba_ref': '00004870000110',
            'nearest_metrotube': None,
            'nearest_motorway': None,
            'nearest_busstop': None,
            'nearest_ohl': None,
            'point': {
                'coordinates': [
                    0.1316297368794871,
                    52.20569063525474
                ],
                'type': 'Point'
            },
            'nearest_greenbelt_distance': None,
            'nearest_substation_distance': None,
            'nearest_motorway_distance': None,
            'nearest_substation': None,
            'nearest_broadband_fast': None
        }, {
            'nearest_school_distance': None,
            'nearest_metrotube_distance': None,
            'geom': {
                'coordinates': [
                    [
                        [
                            [
                                0.13701796531677246,
                                52.2051641218572
                            ],
                            [
                                0.13727545738220215,
                                52.2051641218572
                            ],
                            [
                                0.13727545738220215,
                                52.20546657152671
                            ],
                            [
                                0.13701796531677246,
                                52.20546657152671
                            ],
                            [
                                0.13701796531677246,
                                52.2051641218572
                            ]
                        ]
                    ]
                ],
                'type': 'MultiPolygon'
            },
            'authority': 'Cambridge City Council',
            'uprn': '010090969104',
            'nearest_broadband': None,
            'nearest_ohl_distance': None,
            'nearest_trainstop': None,
            'nearest_trainstop_distance': None,
            'unique_asset_id': None,
            'name': 'Allia Ltd',
            'owner': '',
            'id': 39,
            'nearest_school': None,
            'nearest_broadband_distance': None,
            'nearest_greenbelt': None,
            'nearest_busstop_distance': None,
            'ba_ref': '00004870000011',
            'nearest_metrotube': None,
            'nearest_motorway': None,
            'nearest_busstop': None,
            'nearest_ohl': None,
            'point': {
                'coordinates': [
                    0.1371467113494873,
                    52.20531534669196
                ],
                'type': 'Point'
            },
            'nearest_greenbelt_distance': None,
            'nearest_substation_distance': None,
            'nearest_motorway_distance': None,
            'nearest_substation': None,
            'nearest_broadband_fast': None
        }]

        api_url = '{0}/api/location-search'.format(
            settings.LAND_AVAILABILITY_API_URL)

        responses.add(
            responses.GET, api_url,
            body=json.dumps(json_body), status=200,
            content_type='application/json')

        response = client.get(url, {
            'postcode': 'AA11BB',
            'range_distance': 1000})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 2)

    @pytest.mark.django_db
    @override_settings(STATICFILES_STORAGE=None)
    @responses.activate
    def test_location_details_view(self):
        client = Client()
        url = reverse('location-details', kwargs={'uprn': '010090969113'})

        json_body = {
            'nearest_trainstop': None,
            'nearest_school': None,
            'nearest_motorway': None,
            'nearest_substation_distance': None,
            'geom': {
                'type': 'MultiPolygon',
                'coordinates': [
                    [
                        [
                            [0.13153553009033203, 52.205765731674575],
                            [0.13143360614776609, 52.20569340742784],
                            [0.13174474239349365, 52.20561122064091],
                            [0.13180643320083618, 52.20569669489615],
                            [0.13153553009033203, 52.205765731674575]
                        ]
                    ]
                ]
            },
            'nearest_broadband_distance': 72.26585179,
            'estimated_floor_space': None,
            'uprn': '010090969113',
            'nearest_motorway_distance': None,
            'nearest_school_distance': None,
            'authority': 'Cambridge City Council',
            'nearest_ohl': None,
            'point': {
                'type': 'Point',
                'coordinates': [0.1316297368794871, 52.20569063525474]
            },
            'nearest_metrotube': None,
            'nearest_busstop_distance': None,
            'nearest_greenbelt_distance': None,
            'id': 33,
            'owner': '',
            'nearest_greenbelt': None,
            'nearest_ohl_distance': None,
            'nearest_substation': None,
            'nearest_broadband_fast': True,
            'nearest_trainstop_distance': None,
            'full_address': None,
            'name': 'Test Location 1',
            'nearest_busstop': None,
            'unique_asset_id': '',
            'nearest_metrotube_distance': None,
            'nearest_broadband': 6,
            'ba_ref': '00004870000113'
        }

        api_url = '{0}/api/locations/{1}/'.format(
            settings.LAND_AVAILABILITY_API_URL,
            '010090969113')

        responses.add(
            responses.GET, api_url,
            body=json.dumps(json_body), status=200,
            content_type='application/json')

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('Test Location 1' in str(response.content))
        self.assertTrue('Superfast Broadband' in str(response.content))

    @pytest.mark.django_db
    @override_settings(STATICFILES_STORAGE=None)
    @responses.activate
    def test_search_view_selected_area(self):
        client = Client()
        url = reverse('search')

        json_body = [{
            'nearest_school_distance': None,
            'nearest_metrotube_distance': None,
            'geom': {
                'coordinates': [
                    [
                        [
                            [
                                0.13153553009033203,
                                52.205765731674575
                            ],
                            [
                                0.13143360614776609,
                                52.20569340742784
                            ],
                            [
                                0.13174474239349365,
                                52.20561122064091
                            ],
                            [
                                0.13180643320083618,
                                52.20569669489615
                            ],
                            [
                                0.13153553009033203,
                                52.205765731674575
                            ]
                        ]
                    ]
                ],
                'type': 'MultiPolygon'
            },
            'authority': 'Cambridge City Council',
            'uprn': '010090969147',
            'nearest_broadband': None,
            'nearest_ohl_distance': None,
            'nearest_trainstop': None,
            'nearest_trainstop_distance': None,
            'unique_asset_id': None,
            'name': 'Allia Ltd',
            'owner': '',
            'id': 38,
            'nearest_school': None,
            'nearest_broadband_distance': None,
            'nearest_greenbelt': None,
            'nearest_busstop_distance': None,
            'ba_ref': '00004870000110',
            'nearest_metrotube': None,
            'nearest_motorway': None,
            'nearest_busstop': None,
            'nearest_ohl': None,
            'point': {
                'coordinates': [
                    0.1316297368794871,
                    52.20569063525474
                ],
                'type': 'Point'
            },
            'nearest_greenbelt_distance': None,
            'nearest_substation_distance': None,
            'nearest_motorway_distance': None,
            'nearest_substation': None,
            'nearest_broadband_fast': None
        }, {
            'nearest_school_distance': None,
            'nearest_metrotube_distance': None,
            'geom': {
                'coordinates': [
                    [
                        [
                            [
                                0.13701796531677246,
                                52.2051641218572
                            ],
                            [
                                0.13727545738220215,
                                52.2051641218572
                            ],
                            [
                                0.13727545738220215,
                                52.20546657152671
                            ],
                            [
                                0.13701796531677246,
                                52.20546657152671
                            ],
                            [
                                0.13701796531677246,
                                52.2051641218572
                            ]
                        ]
                    ]
                ],
                'type': 'MultiPolygon'
            },
            'authority': 'Cambridge City Council',
            'uprn': '010090969104',
            'nearest_broadband': None,
            'nearest_ohl_distance': None,
            'nearest_trainstop': None,
            'nearest_trainstop_distance': None,
            'unique_asset_id': None,
            'name': 'Allia Ltd',
            'owner': '',
            'id': 39,
            'nearest_school': None,
            'nearest_broadband_distance': None,
            'nearest_greenbelt': None,
            'nearest_busstop_distance': None,
            'ba_ref': '00004870000011',
            'nearest_metrotube': None,
            'nearest_motorway': None,
            'nearest_busstop': None,
            'nearest_ohl': None,
            'point': {
                'coordinates': [
                    0.1371467113494873,
                    52.20531534669196
                ],
                'type': 'Point'
            },
            'nearest_greenbelt_distance': None,
            'nearest_substation_distance': None,
            'nearest_motorway_distance': None,
            'nearest_substation': None,
            'nearest_broadband_fast': None
        }]

        api_url = '{0}/api/location-search'.format(
            settings.LAND_AVAILABILITY_API_URL)

        responses.add(
            responses.GET, api_url,
            body=json.dumps(json_body), status=200,
            content_type='application/json')

        response = client.get(url, {
            'polygon': """[
                    [
                        [
                            0.0858306884765625,
                            52.18308960259887
                        ],
                        [
                            0.1786994934082031,
                            52.18308960259887
                        ],
                        [
                            0.1786994934082031,
                            52.22485521518378
                        ],
                        [
                            0.0858306884765625,
                            52.22485521518378
                        ],
                        [
                            0.0858306884765625,
                            52.18308960259887
                        ]
                    ]
                ]"""
            })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 2)
