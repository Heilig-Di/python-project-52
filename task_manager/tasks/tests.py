from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from .models import Task
from task_manager.labels.models import Label

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


class TaskFilterTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

        self.status1 = Status.objects.create(name='Status 1')
        self.status2 = Status.objects.create(name='Status 2')
        self.user2 = User.objects.create_user(
            username='executor',
            password='password123'
        )
        self.label1 = Label.objects.create(name='Label 1')
        self.label2 = Label.objects.create(name='Label 2')

        self.task1 = Task.objects.create(
            name='Task 1',
            description='Description 1',
            author=self.user,
            status=self.status1,
            executor=self.user2
        )
        self.task1.labels.add(self.label1)

        self.task2 = Task.objects.create(
            name='Task 2',
            description='Description 2',
            author=self.user2,
            status=self.status2,
            executor=self.user
        )
        self.task2.labels.add(self.label2)

    def test_filter_by_status(self):
        response = self.client.get(reverse('tasks:list'), {
            'status': self.status1.id
        })
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_filter_by_executor(self):
        response = self.client.get(reverse('tasks:list'), {
            'executor': self.user2.id
        })
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')


    def test_filter_by_label(self):
        response = self.client.get(reverse('tasks:list'), {
            'labels': self.label1.id
        })
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')


    def test_filter_self_tasks(self):
        response = self.client.get(reverse('tasks:list'), {
            'self_tasks': 'on'
        })
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

