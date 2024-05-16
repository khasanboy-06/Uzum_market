"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from shop_app.views import home, category, batafsil, create_product, delete_product, update_product
from . import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/<int:id>/', category, name='category'),
    path('batafsil/<int:id>/', batafsil, name='batafsil'),
    path('create_product/', create_product, name='create_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('update_product/<int:id>/', update_product, name='update_product'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
