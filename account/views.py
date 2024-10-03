from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)    # Instanciamos el formulario con los datos enviados
        if form.is_valid():    # Validamos los datos del formulario
            cd = form.cleaned_data
            user = authenticate(    # Si los datos son validos autenticamos con la bd - Creamos el objeto user
                request,
                username=cd['username'],    # Parametros
                password=cd['password']     # Parametros
            )
            if user is not None:
                if user.is_active:    # Verificamos el estado del usuario
                    login(request, user)    # Si el user esta activo llamamos al método login()
                    return HttpResponse('Authenticated succesfully')    # Devolvemos el mensaje de éxito
                else:
                    return HttpResponse('Disabled account')    # Si el user no esta activo
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
