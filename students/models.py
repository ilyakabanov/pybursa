# -*- coding: utf8 -*-

from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    PACKAGE_CHOICES = (
        ('standart', 'Стандартный пакет'),
        ('gold', 'Золотой пакет'),
        ('vip', 'VIP пакет'),
    )
    package = models.CharField(
        max_length=8,
        choices=PACKAGE_CHOICES,
        default='standart',
    )

    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname + ' ' + self.name
