from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=255)
    start_date = models.DateField()

    def __unicode__(self):
        return self.name
