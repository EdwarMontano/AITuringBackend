"""aituringtesttec URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from aituringtesttec import views as local_views
from clientes import views as clientes_views

from datetime import datetime

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', local_views.home_view),

    path('hello/', local_views.helloAlien, name= 'helloAlien'),
    path('sorted/', local_views.sortedNumbers, name= 'sorted'),
    path('greeting/<int:age>/<str:name>/', local_views.greeting, name= 'hi'),

    path('clientes/', clientes_views.list_clientes, name= 'feed'),
    path('clientes/login/',clientes_views.login_view, name= 'login')
] +  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
