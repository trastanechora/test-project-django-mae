from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import FileField
from django.utils import timezone
from django.db import models

class Mentor(models.Model):
    full_name = models.CharField(max_length=50)
    experience = models.TextField(max_length=255)
    quote = models.TextField(max_length=255)
    photo = models.FileField(upload_to='mentor/', null=True, verbose_name="")
    def __str__(self):
        return self.full_name