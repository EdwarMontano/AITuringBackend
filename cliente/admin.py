from django.contrib import admin

from .models import Cliente,Category,Pais,City

admin.site.register(Cliente)
admin.site.register(Category)
admin.site.register(Pais)
admin.site.register(City)
