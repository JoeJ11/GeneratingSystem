from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cluster(models.Model):
    configuration = models.IntegerField()
    user_name = models.CharField(max_length=100)
    def __str__(self):
        return "Configuration {}".format(self.configuration)

class LogItem(models.Model):
    file_name = models.CharField(max_length=100)
    # log_history = models.TextField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    def __str__(self):
        return self.file_name

class Message(models.Model):
    content = models.TextField()
    response = models.TextField(default='')
    meta_data = models.CharField(max_length=100)
    log_item = models.ForeignKey(LogItem, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.content

    def generate_response(self):
        return
