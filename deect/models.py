from datetime import datetime

import django
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255,)
    translation = models.CharField(max_length=255)
    date = models.DateField(default=django.utils.timezone.now)
    tutor = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
