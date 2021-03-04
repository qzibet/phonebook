from django.urls import path
from .views import (
    PhonebookView,
    Search,
)

urlpatterns = [
    path("", PhonebookView.as_view(), name="phonebook_list"),
    path("search/", Search.as_view(), name="search"),
]
