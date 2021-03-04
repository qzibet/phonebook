from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Phonebook


class PhonebookView(ListView):
    model = Phonebook
    queryset = Phonebook.objects.all()
    template_name = "mainapp/base.html"
    paginate_by = 4


class Search(ListView):
    template_name = "mainapp/base.html"
    paginate_by = 15

    def get_queryset(self):
        obj = self.request.GET.get("q")
        try:
            if int(obj):
                return Phonebook.objects.filter(phone=self.request.GET.get("q"))
                # elif obj is int:
                #     print(f"{obj = }")
                #     return Phonebook.objects.filter(phone=self.request.GET.get("q"))
        except Exception:
            if len(obj) == 0:
                return Phonebook.objects.filter(
                    title__icontains=self.request.GET.get("q")
                )
            else:
                print(f"{obj = }")
                return Phonebook.objects.filter(
                    title__icontains=self.request.GET.get("q")
                )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
