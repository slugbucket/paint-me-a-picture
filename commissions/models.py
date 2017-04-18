from django.db import models

# Create your models here.

class CommissionType(models.Model):
    name             = models.CharField(max_length=64, unique=True,null=False)
    days_to_complete = models.IntegerField(default=3)
    active           = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    title            = models.CharField(max_length=128,null=False)
    fullname         = models.CharField(max_length=128,null=False)
    contact_address  = models.CharField(max_length=128,null=False)
    commission_type  = models.ForeignKey(CommissionType,on_delete=models.CASCADE,default=1)
    due_date         = models.DateField('date for customer delivery', null=False)
    comments         = models.TextField

    def __str__(self):
        return self.title

class Commission(models.Model):
    enquiry          = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    commission_type  = models.ForeignKey(CommissionType,on_delete=models.CASCADE)
    def __str__(self):
        #return Enquiry.objects.get(id=self.enquiry_id).title
        return self.enquiry.title
        #return str(self.id)
        #return("bob")
        #return self.enquiry
        #return enquiry.title

    def enquiry_due_date(self):
        #return Enquiry.objects.filter(pk=self.enquiry_id).due_date
        return self.enquiry.due_date

    def title(self):
        #return Enquiry.objects.get(id=self.enquiry_id).title
        return self.enquiry.title
        #return("bob")
        #return enquiry.title
