from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Number_of_Companies_Form(forms.Form):
    NumberOfCompanies = forms.IntegerField(label = 'NumberOfCompanies')#max_length = 200,

class List_of_Companies_Form(forms.Form):
    def __init__(self, NumberOfCompanies, *args, **kwargs):
        super(List_of_Companies_Form, self).__init__(*args, **kwargs)
        for i in range(1,int(NumberOfCompanies)+1):
            self.fields[str(i)] = forms.CharField(label = str(i)) 
