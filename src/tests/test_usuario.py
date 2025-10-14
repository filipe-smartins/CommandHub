from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UsuarioViewsTest(TestCase):
    def test_register_get(self):
        resp = self.client.get(reverse('usuario:register'))
        self.assertEqual(resp.status_code, 200)

    def test_register_post_creates_user(self):
        data = {
            'username': 'tester',
            'email': 'tester@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }
        resp = self.client.post(reverse('usuario:register'), data)
        # After registration should redirect to profile
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(User.objects.filter(username='tester').exists())

    def test_profile_view(self):
        u = User.objects.create_user(username='bob', password='pw')
        resp = self.client.get(reverse('usuario:profile', kwargs={'username': 'bob'}))
        self.assertEqual(resp.status_code, 200)
