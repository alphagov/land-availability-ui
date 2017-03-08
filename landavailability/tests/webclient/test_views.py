from unittest import TestCase
from django.test import override_settings
from django.test import Client
from django.urls import reverse


class WebclientViewTestCase(TestCase):
    @override_settings(STATICFILES_STORAGE=None)
    def test_index_can_be_loaded(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Sign in' in str(response.content))
