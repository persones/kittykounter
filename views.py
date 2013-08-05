import json

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


from kittykounter.models import DoorEvent
from django.utils import timezone
def mainView(request):
    if request.method == "GET":
        lastUpdate = DoorEvent.objects.get(pk=1)
        response_data = {}
        response_data['time'] = lastUpdate.lastdatetime
        response_data['direction'] = lastUpdate.direction
        response_data['kount'] = lastUpdate.kount
        return render(request, 'kittykounter/stats.html', response_data)

@csrf_exempt
def updateView(request):
    print "yes"
    if request.method == "GET":
        lastUpdate = DoorEvent.objects.get(pk=1)
        lastUpdate.lastdatetime = timezone.now()
        lastUpdate.save()
        return HttpResponse(lastUpdate.lastdatetime)
    if request.method == "POST":
        print "post"
        return HttpResponse('post')

def pollView(request):
    if request.method == "GET":
        lastUpdate = LastUpdate.objects.get(pk=1)
        lastUpdate.lastdatetime = timezone.now()
        lastUpdate.save()
        return HttpResponse(lastUpdate.lastdatetime)


#return render(request, 'archman/browser.html', data)

