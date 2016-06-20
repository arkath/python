from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from mtracks.models import Genres, Track
# Create your views here.

def index(request):
    trackList = Track.objects.all()
    context = {'trackList' : trackList}
    return render(request,'tracks/index.html',context)

def tracks(request):
    return index(request)


def track_detail(request, track_id):
    try:
        track_obj = Track.objects.get(pk=track_id)
    except:
        raise Http404("The given Track dosen't Exist")
    return render(request,'tracks/trackDetail.html',{'track_obj': track_obj})
