import hashlib, binascii, os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Picture
# Create your views here.
def getAllPictures(request):
    queryset = Picture.all().order_by('id')
    if queryset:
        qs_json = serializers.serialize('json', queryset, fields=('id', 'file', 'name'))
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucune image enregistré")

def getPicture(request):
    id = request.GET.get("id", "")
    queryset = Picture.objects.filter(id=id)
    if queryset:
        qs_json = serializers.serialize('json', queryset, fields=('id', 'file', 'name'))
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucune image correspondante")

@csrf_exempt
def sendPicture(request):
    try:
        file = request.FILES['file']
        picture_instance = Picture.create(file)
        picture_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("Image ajoutée")


def errorTest(request):
    div_zero = 1/0
