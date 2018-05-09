from django import forms
from django.views.generic import ListView
from .models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'creator', 'created_at', 'finished_at', 'description']
        widgets = {
            'created_at': forms.DateInput(attrs={'class': 'datepicker'}),
            'finished_at': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class TodoListForm(ListView):
    class Meta:
        model = Todo
        fields = '__all__'


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


def __init__(self, args,*kwargs):
    super(RegisterUserForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
        field.widget.attrs = {'class': 'form-control'}