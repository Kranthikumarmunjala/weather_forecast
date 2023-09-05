from django.contrib import admin
from .models import State,District
# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display=['id','state','name','rainfall_type']

class StateAdmin(admin.ModelAdmin):
    list_display=['id','name']


admin.site.register(State,StateAdmin)
admin.site.register(District,DistrictAdmin)
