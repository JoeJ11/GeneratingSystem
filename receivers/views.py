from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import ast
# Create your views here.

from django.http import HttpResponse
from .models import Cluster, LogItem, Message

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def register(request):
    if not request.method == 'POST':
        return HttpResponse("WRONG METHOD")

    params = request.POST
    if not _check_params(params, ['configuration_id', 'user_name', 'file_list']):
        return HttpResponse("ILLEGAL PARAMS")
    cluster = Cluster.objects.filter(configuration=params['configuration_id']).filter(user_name=params['user_name'])
    authorized_files = {}
    init_index = {}
    cluster_index = -1
    if len(cluster) == 0:
        cluster = Cluster(configuration=params['configuration_id'], user_name=params['user_name'])
        cluster.save()
        cluster_index = cluster.id
        for file_name in ast.literal_eval(params['file_list']):
            log_item = cluster.logitem_set.create(file_name=file_name)
            log_item.save()
            authorized_files[file_name] = log_item.id
            init_index[file_name] = 0
    else:
        cluster = cluster[0]
        cluster_index = cluster.id
        for log_item in cluster.logitem_set.all():
            authorized_files[log_item.file_name]=log_item.id
            init_index[log_item.file_name] = log_item.message_set.count()
    return HttpResponse(json.dumps({'file_list':authorized_files, 'init_index':init_index, 'cluster_index':cluster_index}))

@csrf_exempt
def message(request, id):
    if not request.method == 'POST':
        return HttpResponse('WRONG METHOD')

    params = request.POST
    if not _check_params(params, ['content', 'order']):
        return HttpResponse('ILLEGAL PARAMS')
    log_item = LogItem.objects.get(id=id)
    msg = log_item.message_set.create(content=params['content'], order=params['order'])
    msg.generate_response()
    return HttpResponse(json.dumps({'id':msg.id}))

@csrf_exempt
def response(request, id):
    if not request.method == 'GET':
        return HttpResponse('WRONG METHOD')
    cluster = Cluster.objects.get(id=id)
    return HttpResponse(cluster.get_newest_response())

def delete(request, id):
    return HttpResponse("Delete with ID {}".format(id))

def _check_params(params, field_list):
    for item in field_list:
        if not params.has_key(item):
            return False
    return True
