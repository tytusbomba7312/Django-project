from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from calc.models import User, Note
import json
import hashlib

# url = hello/?x=10

# def hello(request):
#     return HttpResponse(f"Hello World! {request.GET['x']}")

# url = hello/10

def hello(request, number):
    return HttpResponse(f"Hello World! {number}")

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if data["operation"] == "+":
        result = data["a"] + data["b"]
    return HttpResponse(f"{result}")

def get_users(request):
    users = User.objects.all()
    users_data = []
    for user in users:
        users_data.append([user.username, user.password])
    return JsonResponse({"user": users_data})

@csrf_exempt
def add_user(request):
    data = json.loads(request.body)
    username = data["username"]
    password = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
    users = User.objects.all()
    for existing_user in users:
        if existing_user.username == username:
            return HttpResponse("User already exists!", status=400)
    user = User(username=username, password=password)
    user.save()
    return JsonResponse({"username":username, "password":password})

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data["username"]
    password = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
    try:
        user = User.objects.get(username=username, password=password)
        user.login_count += 1
        user.save()
        return HttpResponse("Logged successfully!", status=200)
    except:
        return HttpResponse("Wrong username or password!", status=400)

@csrf_exempt
def get_notes(request):
    data = json.loads(request.body)
    username = data["username"]
    password = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
    min_length = data.get("min_length", 0)
    try:
        user = User.objects.get(username=username, password=password)
    except:
        return HttpResponse("Wrong username or password!", status=400)
    notes = Note.objects.filter(user=user)
    notes_data = []
    for note in notes:
        if note.is_longer_than(min_length):
            notes_data.append([note.content])
    return JsonResponse({"notes":notes_data})