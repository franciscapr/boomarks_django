from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']
        
def clean_password2(self):    # Definimos un método para comparar la segundo contraseña con la primera
    cd = self.cleaned_data
    if cd['passwoard'] != cd['password2']:
        raise forms.ValidationError("Passwords don't match.")    # Error de validación si las contraseñas no coinciden
    return cd['password2']

class UserEditForm(forms.ModelForm):    # Permite editar el nombre, apellido y correo electronico
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        
class ProfileEditForm(forms.ModelForm):    # Permite editar los datos del perfil que se guardan en el modelos de perfil 
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']