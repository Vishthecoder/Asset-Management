from dataclasses import field
from django import forms

from .models import Category, location, Asset

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'slug']

class LocationForm(forms.ModelForm):
	class Meta:
		model = location
		fields = ['name', 'city', 'state','country','zipcode','contact_no']

class AssetForm(forms.ModelForm):
	class Meta:
		model = Asset
		fields = ['rfid', 'type','name','purchase_date','warranty_expiry','purchase_type','description','serial_no','location','image','state']