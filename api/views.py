from rest_framework import generics
from assets.models import Asset, Category, location, AssetMaintenance
from .serializers import AssetSerializer, CategorySerializer, LocationSerializer, AssetMaintenanceSerializer, AssetSerializerView,AssetSerializerView2

# Create your views here.

class AssetAPIView(generics.ListAPIView):
	queryset = Asset.objects.all().order_by('-modified_at')
	serializer_class = AssetSerializer

class AssetAPIView2(generics.ListAPIView):
	queryset = Asset.objects.all().order_by('-modified_at')
	serializer_class = AssetSerializerView

class AssetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Asset.objects.all()
	serializer_class = AssetSerializerView

class AssetDetailAPIView2(generics.RetrieveUpdateDestroyAPIView):
	queryset = Asset.objects.all()
	serializer_class = AssetSerializerView2

class CategoryAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class LocationAPIView(generics.ListAPIView):
	queryset = location.objects.all()
	serializer_class = LocationSerializer

class LocationDetailAPIView(generics.RetrieveAPIView):
	queryset = location.objects.all()
	serializer_class = LocationSerializer

class AssetMaintenanceAPIView(generics.ListAPIView):
	queryset = AssetMaintenance.objects.all()
	serializer_class = AssetMaintenanceSerializer

class AssetMaintenanceDetailAPIView(generics.RetrieveAPIView):
	queryset = AssetMaintenance.objects.all()
	serializer_class = AssetMaintenanceSerializer



		