from __future__ import unicode_literals

from django.db import models
import json
import generator
# Create your models here.

class Cluster(models.Model):
    configuration = models.IntegerField()
    user_name = models.CharField(max_length=100)
    def __str__(self):
        return "Configuration {}".format(self.configuration)

    def get_newest_response(self):
        response_list = []
        for log_item in self.logitem_set.all():
            response_list += log_item.get_newest_response()
        return json.dumps(response_list)

class LogItem(models.Model):
    file_name = models.CharField(max_length=100)
    # log_history = models.TextField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    head_order = models.IntegerField(default=0)
    def __str__(self):
        return self.file_name

    def get_newest_response(self):
        msg_set = self.message_set.order_by('-order')
        response_list = []
        for msg in msg_set:
            if msg.order >= self.head_order:
                if len(msg.response) > 0:
                    response_list.append({'response':msg.response,'meta_data':msg.meta_data})
            else:
                break
        if len(msg_set) > 0:
            self.head_order = msg_set[0].order+1
        self.save()
        return response_list

class Message(models.Model):
    content = models.TextField()
    response = models.TextField(default='')
    meta_data = models.CharField(max_length=100)
    log_item = models.ForeignKey(LogItem, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.content

    def generate_response(self):
        self.response = generator.generator.response(self.content)
        self.save()
        return
