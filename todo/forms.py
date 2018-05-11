from django import forms
from django.views.generic import ListView
from .models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_text', 'due_date', 'time', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'datepicker' ,'placeholder': 'Select a date'}),
            'time': forms.TimeInput(attrs={'class': 'time', 'placeholder': 'Select a time'})

        }


class RegisterUserForm(forms.ModelForm):

    name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
            model = UserProfile
            fields = ['name', 'email', 'mobile_no', 'password']


class LoginUserForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


