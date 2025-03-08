from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer
from django.shortcuts import render

class AnimalListAPIView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def home(request):
    animals = Animal.objects.all()  # 取得所有 Animal 資料
    return render(request, 'test.html', {'animals': animals})
