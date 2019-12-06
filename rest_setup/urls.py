"""rest_setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from api.views import (
	UserCreateAPIView,
	UserLoginAPIView,
    ItemCreatView,
    ItemDetailView,
    ItemListView,
    ItemCreatView
    # ListView,
    # DetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('signin/',UserLoginAPIView.as_view(), name="signin"),
    path('list/', ItemListView.as_view(), name='list'),
    path('create/', ItemCreatView.as_view(), name='create'),
    path('detail/<int:item_id>/', ItemDetailView.as_view(), name='detail'),


]



urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)