from django.contrib import admin
from .models import Cliente, Category, Pais, City


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_cliente", "categoria", "pais", "city", "estado")
    #  list_display = ('user', 'phone_number', 'website', 'picture')
    list_display_links = ("pk", "name_cliente")
    list_editable = ("categoria", "pais", "city", "estado")
    search_fields = ("user__email", "name_cliente", "categoria", "pais", "city")
    list_filter = (
        "estado",
        "user_created",
        "user_modifed",
    )


# admin.site.register(Cliente)
admin.site.register(Category)
admin.site.register(Pais)
admin.site.register(City)
