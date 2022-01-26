from django.urls import path
from .views import AssetDetailView, AssetListView


urlpatterns = [
    path('list/', AssetListView.as_view(), name='asset-list'),
    path('<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),
]
