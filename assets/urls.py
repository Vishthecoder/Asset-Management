from django.urls import path
from .views import AssetDetailView, AssetListView, categoryFormView, CategoryListView, locationFormView, assetFormView


urlpatterns = [
    path('list/', AssetListView.as_view(), name='asset-list'),
    path('<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),
    path('category-create/', categoryFormView, name='asset-category-creation'),
    path('location-create/', locationFormView, name='asset-location-creation'),
    path('asset-create/', assetFormView, name='asset-asset-creation'),
    path('category/', CategoryListView.as_view(), name='asset-category'),
]
