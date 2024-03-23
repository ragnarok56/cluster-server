from django.db import models

# Create your models here.
class Host:
    name = models.TextField(blank=False, null=False)
    ipv4 = models.CharField(blank=False, null=False)
