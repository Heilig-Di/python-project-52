from django.test import TestCase
from .models import User
from django.urls import reverse


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            password='password123'
        )

        self.other_user = User.objects.create_user(
            username='otheruser',
            first_name='Other',
            password='123password'
        )

    def test_user_create(self):
        response = self.client.post(reverse('users:create'), {
            'username': 'newuser',
            'first_name': 'Tom',
            'last_name': 'User',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username='newuser').exists())

        user = User.objects.get(username="newuser")
        self.assertEqual(user.first_name, "Tom")
        self.assertEqual(user.last_name, "User")

    def test_user_update(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.post(
            reverse('users:update', args=[self.user.pk]),
            {'first_name': 'Jerry',
             'last_name': 'User',
        })
        self.assertRedirects(response, reverse("users:list"))

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Jerry')
        self.assertEqual(self.user.last_name, 'User')

    def test_other_update(self):
        original_name = self.other_user.first_name
        response = self.client.post(
            reverse('users:update', args=[self.other_user.pk]),
            {'first_name': 'Tuffy'}
        )

        self.user.refresh_from_db()
        self.assertEqual(self.other_user.first_name, original_name)
        self.assertRedirects(response, reverse('users:list'))

    def test_user_delete(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.post(
            reverse('users:delete', args=[self.user.pk])
        )
        self.assertRedirects(response, reverse('users:list'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_other_delete(self):
        self.client.login(username='testuser', password='password123')
        self.client.post(reverse('users:delete', args=[self.other_user.pk]))
        self.assertTrue(User.objects.filter(username='testuser').exists())
