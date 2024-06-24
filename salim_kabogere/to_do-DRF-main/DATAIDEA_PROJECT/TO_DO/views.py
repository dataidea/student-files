from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializers, RegistrationSerializers, ActivitySerializers
from .models import MemberLogin, MemberRegistration, ToDo

# Create your views here.

def login (request):
    if request.method =='POST':
        serializer = LoginSerializers(data=request.POST)
        if serializer.is_valid():
            # perform the login logic here
            username =serializer.validated_data["username"]
            email =serializer.validated_data["email"]
            password =serializer.validated_data["password"]
            return HttpResponse(f'Login Successful! Username {username}')
        else:
            return HttpResponse("Invalid credentials")
    else:
        context ={}
    return render (request, "login.html", context)

def register (request):
    if request.method =='POST':
        serializer = RegistrationSerializers(data=request.POST)
        if serializer.is_valid():
            # save new member for registration
            serializer.save()
            
            return HttpResponse('Registration Successful! Username')
        else:
            return HttpResponse("Invalid registration details")
    else:
        context ={}
    return render (request, "register.html", context)


def homepage (request):
    todos = ToDo.objects.all()
    context= {
        "todos": todos
    }
    return render(request, "index.html", context)

# View for creating new todo activity using POST request
@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        serializer = ActivitySerializers(data=request.data)
        if serializer.is_valid():
            # Save new todo activity
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)