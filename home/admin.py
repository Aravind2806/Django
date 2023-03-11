from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(department)


class docadmin(admin.ModelAdmin):
    list_display=['doc_name','dep_name','doc_image']
    list_editable=['doc_image']

class bookingadmin(admin.ModelAdmin):
    list_display=['id','p_name','booking_date','doc_name','booked_on']

admin.site.register(doctors,docadmin)
admin.site.register(booking,bookingadmin)