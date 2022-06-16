import os
import json
from urllib import response
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, UserRegisterSerializer, UserSerializerAll

from .models import User

# Create your views here.

def api_view(request):
    return HttpResponse("This is api page")

def visits_view(request):
    return JsonResponse({"all": [1,2,3]})

@csrf_exempt
def user(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = UserRegisterSerializer(data=data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
            
        serializer.save()
        return JsonResponse(serializer.data, status=201)
        
    elif (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            return HttpResponse(status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=404)

@csrf_exempt
def users_all(request):
    if(request.method == 'GET'):
        users = User.objects.all()
        serializer = UserSerializerAll(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=404)  


@csrf_exempt
def notes_handler(request, path):
    script_dir = os.path.dirname(__file__)
    file_location = os.path.join(script_dir, f'assets/audio/{path}')
    try:
        with open(file_location, 'rb') as f:
            file_data = f.read()
            
        response = HttpResponse(file_data, content_type='audio/mp3')
        
    except IOError:
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response


@csrf_exempt
def json_handler(request, path):
    script_dir = os.path.dirname(__file__)
    file_location = os.path.join(script_dir, f'assets/json/{path}')
    try:
        with open(file_location) as f:
            file_data = json.load(f)

        response = JsonResponse(file_data, safe=False)
        
    except IOError:
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response