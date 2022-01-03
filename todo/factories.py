"""App factories module"""
from functools import partial
from factory import (
    Faker,
    SubFactory,
)
from factory.django import DjangoModelFactory as Factory
from .models import (
    Category,
    Todo,
)


Faker = partial(Faker, locale="fr_FR")  # pylint: disable=invalid-name


class CategoryFactory(Factory):  # pylint: disable=too-few-public-methods
    """Category Factory"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Metaclass for CategoryFactory"""
        model = Category

    name = Faker("word")


class TodoFactory(Factory):
    """Todo Factory"""

    class Meta:
        """Metaclass for TodoFactory"""
        model = Todo

    title = Faker('word')
    detail = Faker('text')
