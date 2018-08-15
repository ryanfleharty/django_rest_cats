from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Cat
from .serializers import CatSerializer
# Create your views here.
@csrf_exempt
def cats_list(request):
    print("HI GETTING CATS")
    if request.method == "GET":
        cats = Cat.objects.all()
        serial_cats = CatSerializer(cats, many=True)
        return JsonResponse(serial_cats.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serial_cat = CatSerializer(data=data)
        if serial_cat.is_valid():
            serial_cat.save()
            return JsonResponse(serial_cat.data, status=201)
        return JsonResponse(serial_cat.errors, status=400)
