from django.contrib import admin

# Register your models here.
from .models import Enquiry, Commission, CommissionType

admin.site.register(Enquiry)
admin.site.register(Commission)
admin.site.register(CommissionType)
