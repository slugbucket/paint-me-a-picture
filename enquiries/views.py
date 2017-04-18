from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from commissions.models import Commission, Enquiry
from enquiries.forms import EnquiryForm

# Create your views here.
def index(request):
    new_enq = EnquiryForm()
    template = loader.get_template('enquiries/index.html')
    context = {
        'new_enq': new_enq,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Paint me a picture enquiries front page.<br />Display the activity calendar and request form.")

"""
Function to take the POSTed form and save the details in the database
"""
def create_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enq = form.save()
            return redirect('detail', enquiry_id=enq.pk)
    else:
        form = EnquiryForm()
        template = loader.get_template('enquiries/index.html')
        context = {
            'new_enq': new_enq,
        }
        return HttpResponse(template.render(context, request))
        #return render(request, 'blog/post_edit.html', {'form': form})

"""
Function to show the detail of an enquiry
"""
def detail(request, enquiry_id):
    enq = Enquiry.objects.get(id=enquiry_id)
    template = loader.get_template('enquiries/detail.html')
    context = {
        'enq': enq,
    }
    return HttpResponse(template.render(context, request))

