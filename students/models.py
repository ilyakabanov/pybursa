# -*- coding: utf8 -*-

from django.db import models


class Student(models.Model):
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Фамилия', max_length=255)
    date_of_birth = models.DateField('Дата рождения')
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=15)

    PACKAGE_CHOICES = (
        ('standart', 'Стандартный пакет'),
        ('gold', 'Золотой пакет'),
        ('vip', 'VIP пакет'),
    )
    package = models.CharField(
        'Пакет',
        max_length=8,
        choices=PACKAGE_CHOICES,
        default='standart',
    )

    courses = models.ManyToManyField('courses.Course', verbose_name='Курсы')
    dossier = models.OneToOneField(
        'students.Dossier',
        verbose_name='Досье',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.surname + ' ' + self.name


class Dossier(models.Model):
    adress = models.ForeignKey('courses.Address', verbose_name='Адрес')
    unloved_courses = models.ManyToManyField(
        'courses.Course',
        verbose_name='Нелюбимые курсы',
        blank=True,
        null=True,
    )

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
        'Любимый цвет',
        max_length=10,
        choices=COLOR_CHOICES,
        default='green',
    )

    def __unicode__(self):
        return u"Досье №%d" % self.id
