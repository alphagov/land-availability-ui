from unittest import TestCase
from django.test import override_settings
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
import pytest


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
