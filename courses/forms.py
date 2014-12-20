# -*- coding: utf8 -*-

from django import forms

from pybursa.forms import BaseForm
from courses.models import Course, Address
from coaches.models import Coach


class CourseForm(BaseForm):

    def lable(name):
        return Course._meta.get_field_by_name(name)[0].verbose_name

    lang = forms.ChoiceField(label=lable('lang'), choices=Course.LANG_CHOICES)
    name = forms.CharField(label=lable('name'), max_length=255)
    slug = forms.SlugField(label=lable('slug'), required=False, max_length=255)
    description = forms.CharField(label=lable('description'))
    coach = forms.ModelChoiceField(
        Coach.objects.filter(role='coach'),
        label=lable('coach'),
    )
    assistant = forms.ModelChoiceField(
        Coach.objects.filter(role='asist'),
        label=lable('assistant')
    )
    start_date = forms.DateField(label=lable('start_date'))
    end_date = forms.DateField(label=lable('end_date'))
    venue = forms.ModelChoiceField(
        Address.objects.all(),
        required=False,
        label=lable('venue')
    )
