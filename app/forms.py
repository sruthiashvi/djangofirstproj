from django import forms
from .models import TodosModel
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class TodosForm(forms.Form):
    name=forms.CharField(max_length=250)
    completed=forms.BooleanField()