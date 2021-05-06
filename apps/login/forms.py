from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import *


class CreateUserForm(UserCreationForm):
    password1 = CharField(max_length=100, widget=PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = CharField(max_length=100, widget=PasswordInput(attrs={'placeholder': 'Repetir Contraseña'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': TextInput(attrs={
                'placeholder':'Usuario',
                'id':'usuario'
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Correo electrónico',
                'required':'true'
            }),

        }