#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Commission, Enquiry
from enquiries.forms import EnquiryForm

# Create your views here.
def index(request):
    #return HttpResponse("Paint me a picture commissions index.")
    commission_list = Commission.objects.all()
    template = loader.get_template('commissions/index.html')
    context = {
        'commissions': commission_list,
    }
    return HttpResponse(template.render(context, request))

"""
"""
def show(request, commission_id):
    response = "Displaying the contents of commission %s."

