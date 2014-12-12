# -*- coding: utf8 -*-

from django.db import models


class Course(models.Model):
    LANG_CHOICES = (
        ('php', 'PHP 5.5'),
        ('js', 'JavaScript'),
        ('python', 'Python 2.7'),
        ('rails', 'Ruby in Rails'),
    )
    lang = models.CharField(
        'Язык',
        max_length=8,
        choices=LANG_CHOICES,
        default='python'
    )
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('URL', default='')
    description = models.CharField('Описание', max_length=255)
    coach = models.ForeignKey(
        'coaches.Coach',
        verbose_name='Тренер',
        limit_choices_to={'role': 'coach'}
    )
    assistant = models.ForeignKey(
        'coaches.Coach',
        verbose_name='Асистент',
        limit_choices_to={'role': 'asist'},
        related_name='assistant',
    )
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    venue = models.ForeignKey(
        'courses.Address',
        verbose_name='Место',
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.name


class Address(models.Model):
    zcode = models.IntegerField('Индекс')
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=100)
    district = models.CharField('Район', max_length=100)
    street = models.CharField('Улица', max_length=100)
    home = models.CharField('Дом', max_length=10)

    def __unicode__(self):
        return "%s, %s, %s %s" % (self.country, self.city, self.street, self.home)
