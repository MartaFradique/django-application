from django.shortcuts import render, redirect
from .models import Room
from .models import Topic
from django.db.models import Q
from .forms import RoomForm

# # Create your views here.
# roms = [
#     {
#         'id': 1,
#         'name': 'I cant solve this python problem',
#     },
#      {
#         'id': 2,
#         'name': 'I am having this problem with django',
#     },
#      {
#         'id': 3,
#         'name': 'My react list isnt rendering',
#     },
# ]


def home(request):
    rooms = Room.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = rooms.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q)|
        Q(description__icontains = q)
        )
    count = rooms.count()
    print(count)
    topic = Topic.objects.all()
    context = {'rooms': rooms, 'topic': topic, 'room_count': count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    context ={'form': form}
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj':room})
    