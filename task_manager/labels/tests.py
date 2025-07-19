from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Label
from tasks.models import Task

User = get_user_model()

class LabelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

        self.label = Label.objects.create(name='label1')


    def test_label_create(self):
        response = self.client.post(
            reverse('labels:create'),
            {'name': 'Urgent'}
        )
        self.assertTrue(Label.objects.filter(name='Urgent').exists())


    def test_label_update(self):
        response = self.client.post(
            reverse('labels:update', args=[self.label.pk]),
            {'name': 'Update label'}
        )
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Update label')


    def test_label_delete(self):
        response = self.client.post(
            reverse('labels:delete', args=[self.label.pk])
        )

        if Label.objects.filter(pk=self.label.pk).exists():
            self.assertTrue(Label.objects.filter(pk=self.label.pk).exists())

        else:
            self.assertFalse(Label.objects.filter(pk=self.label.pk).exists())

