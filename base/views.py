from django.shortcuts import render
# Create your views here.
roms = [
    {
        'id': 1,
        'name': 'I cant solve this python problem',
    },
     {
        'id': 2,
        'name': 'I am having this problem with django',
    },
     {
        'id': 3,
        'name': 'My react list isnt rendering',
    },
]


def home(request):
    context = {'roms': roms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for r in roms:
        if r['id'] == int(pk):
            room = r
            break
    context = {'room': room}
    return render(request, 'base/room.html', context)