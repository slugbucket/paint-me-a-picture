from django.forms import ModelForm
from commissions.models import Enquiry


"""
 Based on https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
"""
class EnquiryForm(ModelForm):
    #title           = forms.CharField(max_length=128)
    #fullname        = forms.CharField(max_length=128)
    #contact_address = forms.EmailField()
    #due_date        = forms.DateField()
    #details         = forms.CharField(widget=forms.TextArea)
    #commission_type = forms.SelectField(options=CommissiinType.objects.all())
    class Meta:
        model = Enquiry
        fields = ['title', 'fullname', 'contact_address', 'due_date', 'commission_type']
