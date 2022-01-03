from django.test import TestCase
from todo.models import Todo


class ModelsTestCase(TestCase):
    def setUp(self):
        todo = Todo.objects.create(title="My first todo")

        todo.title = " Doe"
        todo.save()
        self.assertEqual(todo.title)
