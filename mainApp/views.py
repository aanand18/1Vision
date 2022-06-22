from re import L
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id' : 1, 'name' : 'Lets learn python!'},
#     {'id' : 2, 'name' : 'DS and Algos!'},
#     {'id' : 3, 'name' : 'Front End Development!'},
    
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'mainApp/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'mainApp/room.html', context)

def createRoom(request):
    form = RoomForm

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'mainApp/room_form.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'mainApp/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'mainApp/delete.html', {'obj': room})