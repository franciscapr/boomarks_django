from django import forms
from django.contrib.auth import get_user_model

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