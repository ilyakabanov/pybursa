from django.db import models
from courses.models import Course

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Student(models.Model):

    PACKAGE_CHOICES = (
        ('standart', 'Standart'),
        ('gold', 'Gold'),
        ('vip', 'VIP'),
        )

    name = models.CharField('NA-ME', max_length=255)
    slug = models.SlugField()
    surname = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField(help_text="Not unical email")
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15, choices=PACKAGE_CHOICES, db_index=True)
    note = models.TextField(blank=True, null=True)
    # is_active = models.BooleanField()
    group = models.ForeignKey(Group, related_name='students')
    kurator_group = models.ForeignKey(Group, related_name='kurators')
    courses = models.ManyToManyField(Course)


    def __unicode__(self):
        return self.name + ' ' + self.surname