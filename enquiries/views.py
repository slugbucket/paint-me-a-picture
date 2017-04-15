#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Paint me a picture enquiries front page.<br />Display the activity calendar and request form.")
