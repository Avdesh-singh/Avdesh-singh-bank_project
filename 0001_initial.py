from django import forms
from .models import Account

class RegisterationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','dob','address','email','state','gender','phone','aadhar','photo']

