from rest_framework import serializers
from assets.models import Asset,  Category, location, AssetMaintenance

class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = location
		fields = ('__all__')

class AssetMaintenanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = AssetMaintenance
		fields = ('__all__')