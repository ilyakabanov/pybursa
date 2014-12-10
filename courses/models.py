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
        max_length=8,
        choices=LANG_CHOICES,
        default='python'
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    coach = models.ForeignKey('coaches.Coach', limit_choices_to={'role': 'coach'})
    assistant = models.ForeignKey(
        'coaches.Coach',
        limit_choices_to={'role': 'asist'},
        related_name='assistant',
    )
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey('courses.Address', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    zcode = models.IntegerField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    home = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s, %s, %s %s" % (self.country, self.city, self.street, self.home)
