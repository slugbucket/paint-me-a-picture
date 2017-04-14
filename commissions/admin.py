from django.contrib import admin

# Register your models here.
from .models import Commission, CommissionType

admin.site.register(Commission)
admin.site.register(CommissionType)
