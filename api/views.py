import os
import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserScoreSerializer, UserSerializer, UserRegisterSerializer, UserSerializerAll, UserTelegramSerializer

from .models import User
from telegrambot.bot import bot

# Create your views here.
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


@csrf_exempt
def username_data(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse(status=404)

    if (request.method == "GET"):
        serializer = UserScoreSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserScoreSerializer(user, data=data)
        
        if serializer.is_valid():
            if serializer.validated_data['bestSpeed'] > user.__dict__['bestSpeed']:
                serializer.save()
                send_score(request, username)

            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def send_score(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse(status=404)
    
    user = user.__dict__
    for id in user['telegram']:
        bot.send_message(chat_id=id, text=f"Пользователь {username}, только что улучшил совй рекорд! Теперь это {user['bestSpeed']}")
    return HttpResponse(status=200)