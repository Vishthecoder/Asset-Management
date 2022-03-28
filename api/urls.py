from django.urls import path
from .views import AssetAPIView, AssetDetailAPIView, LocationAPIView, LocationDetailAPIView, CategoryAPIView, CategoryDetailAPIView, AssetMaintenanceAPIView, AssetMaintenanceDetailAPIView 


urlpatterns = [
    path('', AssetAPIView.as_view()),
    path('<int:pk>/', AssetDetailAPIView.as_view()),
    path('location/', LocationAPIView.as_view()),
    path('location/<int:pk>/', LocationDetailAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('maintenance/', AssetMaintenanceAPIView.as_view()),
    path('maintenance/<int:pk>/', AssetMaintenanceDetailAPIView.as_view()),
]
