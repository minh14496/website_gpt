from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

def main(request):
    # return HttpResponse('Hello World!')
    
    # render using html
    return render(request, 'hello.html', {'name': 'Minh'})

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer