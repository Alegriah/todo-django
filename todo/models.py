from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=20,
    )
    date = models.DateTimeField(
        verbose_name=_("date"),
        default=timezone.now,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=100,
    )
    detail = models.TextField(
        verbose_name=_("detail")
    )
    date = models.DateTimeField(
        verbose_name=_("date"),
        default=timezone.now,
    )
    category = models.ManyToManyField('Category', related_name='todos')
    done = models.BooleanField(
        verbose_name=_("done"),
        default=False,
    )

    def __str__(self):
        return self.title
