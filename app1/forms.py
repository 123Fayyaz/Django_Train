from django import forms
from app1.models import Train_Details
class train_form(forms.ModelForm):
    # train_num=forms.IntegerField()
    # train_name=forms.CharField()
    # Origin_city =forms.CharField()
    # destination_city =forms.CharField()
    # departure_time=forms.TimeField()
    # arrival_time=forms.TimeField()
    class Meta:
        model=Train_Details
        field='__all__'