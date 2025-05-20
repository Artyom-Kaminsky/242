from django.contrib import admin

from clients.models import Client
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ("email", "username", "date_created", "is_superuser")
    search_fields = ("email", "username")
    list_filter = ("date_created", "gender")
    list_per_page = 50


# admin.site.register(Client, ClientAdmin)