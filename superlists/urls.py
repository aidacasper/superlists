"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from lists import views
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
        re_path(r'^$', views.home_page, name='home'),
        re_path(r'^lists/', include(list_urls)),    
] 

urlpatterns += static(settings.STATIC_URL)
