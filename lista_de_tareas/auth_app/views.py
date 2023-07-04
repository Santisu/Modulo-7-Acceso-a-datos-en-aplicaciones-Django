from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
class LoginView(View):
    form = LoginForm()
    def get(self, request):
        context = {"form": self.form}
        return render(request, 'login.html', context)
    def post(self, request):
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            context = {"form": self.form,
                       'error': "El usuario o contraseña ingresada no son correctos"}
            return render(request, 'login.html', context)
        else:
            login(request, usuario)
            return redirect('index_user')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('index')
