from django.shortcuts import render
from django.http import Http404
import traceback
from mtracks.models import Genres, Track
# Create your views here.

def index(request):
    try:
        trackList = Track.objects.all()
        genresList = Genres.objects.all()
        context = {
            'index' : {
                'trackList':trackList,
                'genresList':genresList
            }
        }
    except:
        raise Http404("Exception in index function in views of mtracks app ")
    return render(request,'home/index.html',context)

def tracks(request):
    try:
        trackList = Track.objects.all()
        context = {
                'trackList':trackList,
            }
    except:
        raise Http404("Exception in index function in views of mtracks app ")
    return render(request,'tracks/index.html',context)

def detail(request,id):
    try:
        uri = request.get_raw_uri()
        g_obj = {}
        t_obj = {}

        if str(uri).__contains__("genre"):
            g_obj = Genres.objects.get(pk=id)
            templateUri = "genre/genreDetail.html"
        elif str(uri).__contains__("track"):
            t_obj = Track.objects.get(pk=id)
            templateUri = "track/trackDetail.html"
        context = {"index":{"t_obj":t_obj,"g_obj":g_obj}}
    except:
        raise "some problem encountered"
    try:
        return render(request,templateUri,context)
    except:
        raise "missing variables"


def genres(request):
    try:
        genresList = Genres.objects.all()
        context = {
            'genresList':genresList,
            }
    except:
        raise Http404("Exception in genres function in views of mtracks app ")
    return render(request,'genres/index.html',context)


