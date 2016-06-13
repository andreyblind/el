from django.db import models

class recipes(models.Model):
    url = models.CharField(max_length=100)

