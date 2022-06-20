from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

rooms = [
    {'id' : 1, 'name' : 'Lets learn python!'},
    {'id' : 2, 'name' : 'DS and Algos!'},
    {'id' : 3, 'name' : 'Front End Development!'},
    
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'mainApp/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'mainApp/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'mainApp/room_form.html', context)