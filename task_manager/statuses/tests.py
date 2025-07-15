from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        self.status = Status.objects.create(name='Test Status')


    def test_status_create(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('statuses:create'),
            {'name': 'New Status'}
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())


    def test_status_update(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('statuses:update', args=[self.status.pk]),
            {'name': 'Updated Status'}
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')


    def test_status_delete(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('statuses:delete', args=[self.status.pk])
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
