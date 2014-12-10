# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    ROLE_CHOICES = (
        ('coach', 'Тренер'),
        ('asist', 'Асистент'),
    )
    role = models.CharField(
        max_length=5,
        choices=ROLE_CHOICES,
        default='coach',
    )

    user = models.ForeignKey(User)
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name
