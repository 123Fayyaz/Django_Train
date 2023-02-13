from django import forms
from train_fare.models import fare
# Create your models here.
class enter_fare(forms.ModelForm):
    class Meta:
        model=fare
        fields='__all__'