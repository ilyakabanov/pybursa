from django.db import models
from django.utils import timezone


class Course(models.Model):

    name = models.CharField(max_length=255)
    start_date = models.DateField()

    def __unicode__(self):
        return self.name

    def is_in_future(self):
    	return self.start_date > timezone.now().date()