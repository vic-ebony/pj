from rest_framework import generics
from django.shortcuts import render
from .models import Animal, Hall
from .serializers import AnimalSerializer

class AnimalListAPIView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def home(request):
    halls = Hall.objects.all()  # 取得所有館別
    hall_id = request.GET.get('hall_id')  # 讀取 URL 中的館別篩選參數
    if hall_id:
        animals = Animal.objects.filter(hall_id=hall_id)
    else:
        animals = Animal.objects.all()
    return render(request, 'test.html', {'animals': animals, 'halls': halls})
