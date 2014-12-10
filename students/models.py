# -*- coding: utf8 -*-

from django.db import models


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

    courses = models.ManyToManyField('courses.Course')
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name


class Dossier(models.Model):
    adress = models.ForeignKey('courses.Address')
    unloved_courses = models.ManyToManyField('courses.Course', blank=True, null=True)
    
    COLOR_CHOICES = (
        ('ref', 'Красный'),
        ('orange', 'Оранжевый'),
        ('yellow', 'Желтый'),
        ('green', 'Зеленый'),
        ('lightblue', 'Голубой'),
        ('blue', 'Синий'),
        ('purple', 'Фиолетовый'),
    )
    color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        default='green',
    )


    def __unicode__(self):
        return u"Досье №%d" % self.id