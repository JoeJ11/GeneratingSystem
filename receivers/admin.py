from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Cluster)
admin.site.register(LogItem)
admin.site.register(Message)
