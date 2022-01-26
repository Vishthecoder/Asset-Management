from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

from .models import Asset

class AssetListView(ListView):
	model = Asset
	template_name = "asset/index.html"


class AssetDetailView(DetailView):
	model = Asset
	template_name = "asset/detail.html"