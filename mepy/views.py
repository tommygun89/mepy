from django.http import HttpResponse
from django.shortcuts import render

from mepy.CircullumVitae import CircullumVitae
from mepy.About import About


def index(request):
    return render(request, 'base.html')


def circullumVitae(request):
    return CircullumVitae().respond()


def aboutMe(request):
    return About().respond()
