from django.contrib import admin
from .models import Phonebook


@admin.register(Phonebook)
class PhonebookAdmin(admin.ModelAdmin):
    list_display = ["title", "phone"]
    search_fields = ["title", "phone"]