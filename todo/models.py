from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todoing(models.Model):
    subject     =   models.CharField(max_length=200)
    task        =   models.TextField(max_length=200)
    date        =   models.DateField(blank=False, null=False)
    class Meta:
        verbose_name_plural  =  'Todoing'

    def __str__(self):
        return self.subject
