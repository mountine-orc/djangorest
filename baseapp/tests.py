from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='temporary', email='jlennon@beatles.com', password='temporary')

    def test_index_view_no_login(self):
        """
        If user no login, show hem message
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please login to see this page.")

    def test_index_view_login(self):
        """
        If user is logged in
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('baseapp:index'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('baseapp:index'), follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Load last currency rates")
