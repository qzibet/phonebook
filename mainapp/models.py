from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Phonebook(models.Model):
    title = models.CharField("Имя контакта", max_length=100)
    phone = PhoneNumberField(
        "Номер телефона",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
