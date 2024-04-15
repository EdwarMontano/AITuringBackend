from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import Inicio, pageBlank, pageNoFound, salir

# from django.contrib.auth import login,logout
# from django.contrib.auth.decorators import login_required
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
