from django.contrib import admin
from .models import Category, Asset, location, AssetMaintenance
# Register your models here.

from django.contrib.admin import AdminSite

admin.site.site_header = 'Asset Management'
admin.site.site_title = 'Asset Management'
admin.site.index_title = 'Asset Management'



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',),}
	search_fields = ('name',)
	ordering = ('-name',)

class AssetAdmin(admin.ModelAdmin):
	list_display = ('name','serial_no','rfid','type','state','location')
	search_fields = ('name','serial_no','rfid')
	list_filter = ['type','location']
	search_help_text = "Model Admin"

class AssetMaintenanceAdmin(admin.ModelAdmin):
	list_display = ('maintenance_id','asset_id','maintenance_description','maintenance_date','performed_by','maintenance_cost')
	search_fields = ('maintenance_id',)
	list_filter = ['maintenance_date']

class LocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'city','contact_no')
	ordering = ('-name',)
	search_fields = ('name',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Asset,AssetAdmin)
admin.site.register(location,LocationAdmin)
admin.site.register(AssetMaintenance,AssetMaintenanceAdmin)

