from django import forms
from django.forms import widgets

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('qrcode', )

        labels = {

        }

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "passport": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "telfon": forms.TextInput(attrs={"class": "form-control"}),
            "qayerga": forms.Select(attrs={"class": "form-control"}),
            "test_olindi": forms.DateTimeInput(attrs={"class": "form-control datetimefield", "type": "datetime-local"}),
            "natija_chiqdi": forms.DateTimeInput(attrs={"class": "form-control datetimefield", "type": "datetime-local"}),
        }

        