from django.shortcuts import render
from . import models
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def centerslocationapi(request):
    if request.method == 'GET':
        snippets = models.pokemoncenters.objects.all()
        serializer = serializers.pokemoncenterslocationSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.pokemoncenterslocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def centersapi(request):
    if request.method == 'GET':
        snippets = models.pokemoncenters.objects.all()
        serializer = serializers.pokemoncentersSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.pokemoncentersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
def home(request):
    allpokecenters = models.pokemoncenters.objects.all()
    context = {
        "allpokecenters":allpokecenters
    }
    return render(request, 'base.html',context)