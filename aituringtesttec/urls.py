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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import login,logout
# from django.contrib.auth.decorators import login_required

from .views import *

# from apps.clientes import views as clientes_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cliente/", include(("cliente.urls", "cliente"))),
    path("", login_required(Inicio.as_view()), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("salir/", salir, name="salir"),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    # path('accounts/login',login,{'template_name': 'login.html'}, name = 'login'),
    # path('logout/',logout, name = 'logout'),
    path("pagenotfound/", pageNoFound, name="page404"),
    path("blank/", pageBlank, name="pageblank"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
