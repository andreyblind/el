from django.db import models

class recipes_url(models.Model):
    url = models.CharField(max_length=350)

