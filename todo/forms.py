from django import forms
from django.views.generic import ListView
from .models import *


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['todo_text', 'due_date', 'time', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'datepicker form-control' ,'placeholder': 'Select a date'}),
            'time': forms.TimeInput(attrs={'class ': 'time form-control', 'placeholder': 'HH:MM:SS'}),
            'todo_text': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegisterUserForm(forms.ModelForm):

    username = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50, help_text='Required')
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
            model = UserProfile
            fields = ['username', 'email', 'mobile_no', 'password']


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

