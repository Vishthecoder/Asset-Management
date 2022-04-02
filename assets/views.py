from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib import messages

# Create your views here.

from .models import Asset, Category, location
from .forms import CategoryForm, LocationForm, AssetForm


"""
	VIEWS
"""

class AssetListView(ListView):
	model = Asset
	
	template_name = "asset/index.html"

	def get_context_data(self, **kwargs):        
		context = super().get_context_data(**kwargs)		
		context['asset_count'] = Asset.objects.all().count()
		return context



class AssetDetailView(DetailView):
	model = Asset
	template_name = "asset/detail.html"

class CategoryListView(ListView):
	model = Category
	
	template_name = "asset/category.html"

	def get_context_data(self, **kwargs):        
		context = super().get_context_data(**kwargs)		
		context['category_count'] = Asset.objects.all().count()
		return context


"""
	FORM
"""
def categoryFormView(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Category is Successfully Added.'))
		else:
			messages.success(request,'Error saving form')
		
		return redirect('asset/list/')
	
	form = CategoryForm()
	return render(request=request, template_name= 'asset/category-creation.html', context= {'form':form})


def locationFormView(request):
	if request.method == "POST":
		form = LocationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Location is Successfully Added.'))
		else:
			messages.success(request,'Error saving form')
		
		return redirect('asset/list/')
	
	form = LocationForm()
	return render(request=request, template_name= 'asset/location-creation.html', context= {'form':form})

def assetFormView(request):
	if request.method == "POST":
		form = AssetForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,('Asset is Successfully Added.'))
		else:
			messages.success(request,'Error saving form')
		
		return redirect('asset/list/')
	
	form = AssetForm()
	return render(request=request, template_name= 'asset/asset-creation.html', context= {'form':form})
	
