from django.db import models

# Create your models here.
from coaches.models import Coach
from students.models import Address


class Course(models.Model):
    TECHNOLOGY_CHOICE = (('p', 'Python'),
                         ('r', 'Ruby'),
                         ('j', "JavaScript"))
    name = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey('coaches.Coach', related_name="coach")
    assistant = models.ForeignKey('coaches.Coach', blank=True,
                                  related_name="assistant", null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    technology = models.CharField(max_length=255, choices=TECHNOLOGY_CHOICE)
    venue = models.ForeignKey('students.Address', null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, default="")

    def __unicode__(self):
        return "%s (%s) - %s" % (self.name, self.coach,
                                 self.get_technology_display())