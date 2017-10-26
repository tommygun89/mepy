from django.http import HttpResponse

from mepy.CircullumVitae import CircullumVitae
from mepy.About import About

def index(request):
    return HttpResponse("index")

def circullumVitae(request):
    return CircullumVitae().respond()

def aboutMe(request):
    return About().respond()
