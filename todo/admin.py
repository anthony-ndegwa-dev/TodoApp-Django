from django.contrib import admin
from .models import Todoing

# Register your models here.
class TodoingAdmin(admin.ModelAdmin):
    list_display = ("subject", "task", "date")

admin.site.register(Todoing, TodoingAdmin)
