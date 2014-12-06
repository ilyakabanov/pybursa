from django.db import models

from coaches.models import Coach


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
    coach = models.ForeignKey(Coach, limit_choices_to={'type': 'coach'})
    assistant = models.ForeignKey(
        Coach,
        limit_choices_to={'type': 'asist'},
        related_name='assistant',
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name
