"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Asset API'
API_DESCRIPTION = 'A Web API for creating, updating and editing Assets.'
schema_view = get_swagger_view(title=API_TITLE) 

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',include('users.urls')),
    path('asset/',include('assets.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
