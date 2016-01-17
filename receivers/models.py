from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cluster(models.Model):
    log_type = models.IntegerField()
    log_history = models.TextField()

class LogItem(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    configuration = models.IntegerField()
