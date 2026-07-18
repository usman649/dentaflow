from django.contrib import admin
from apps.clinic.models import (
    Region,
    Treatment,
    TreatmentType,
    Service,
    Material
)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['id','patient','doctor','treatment_type','start_date']
    list_display_links = ['patient','doctor','treatment_type','start_date']
    search_fields = ['patient','doctor','treatment_type','start_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','duration_minutes','treatment_type','is_active']
    list_display_links = ['name','price','duration_minutes','treatment_type','is_active']
    search_fields = ['name','price','duration_minutes','treatment_type','is_active']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id','name','service','quantity']
    list_display_links = ['name','service','quantity']
    search_fields = ['name','service','quantity']

