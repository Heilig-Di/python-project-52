from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from .models import Task

User = get_user_model()

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='123password'
        )
        self.status = Status.objects.create(name='Test Status')
        self.task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            status=self.status,
            author=self.user
        )


    def test_task_create(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('tasks:create'),
            {
                'name': 'New Task',
                'description': 'New Description',
                'status': self.status.id,
            }
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertTrue(Task.objects.filter(name='New Task').exists())


    def test_task_update(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('tasks:update', args=[self.task.pk]),
            {
                'name': 'Updated Task',
                'description': 'Updated Description',
                'status': self.status.id,
            }
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')


    def test_task_detail(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse('tasks:detail', args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')


    def test_task_delete_by_author(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(
            reverse('tasks:delete', args=[self.task.pk])
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())


    def test_task_delete_by_other_user(self):
        self.client.login(username='otheruser', password='123password')
        response = self.client.post(
            reverse('tasks:delete', args=[self.task.pk])
        )
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())
