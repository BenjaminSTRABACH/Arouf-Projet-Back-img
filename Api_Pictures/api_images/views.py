import hashlib, binascii, os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import redirect

from .models import Picture


@csrf_exempt
def getAllPictures(request):
    queryset = Picture.objects.all().order_by('id')
    if queryset:
        qs_json = serializers.serialize('json', queryset, fields=('id', 'file', 'name'))
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucune image enregistrée")


@csrf_exempt
def getPicture(request):
    id = request.GET.get("id", "")
    queryset = Picture.objects.filter(id=id).exists()
    if queryset:

        return redirect("http://localhost:8001/media/" + str(Picture.objects.get(id=id).file))
    else:
        return HttpResponse("Aucune image correspondante")


@csrf_exempt
def sendPicture(request):
    try:
        file = request.FILES['file']
        picture_instance = Picture.create(file, file.name)
        picture_instance.save()
    except Exception as e:
        return HttpResponse("Erreur lors de l'import de l'image", status=400)

    return redirect("/pictures/get/all")


def errorTest(request):
    div_zero = 1/0
