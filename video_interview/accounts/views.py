from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import get_user_model, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # 🔑 Redirection selon le rôle
            if user.role == 'recruiter':
                return redirect('dashboard_recruiter')
            else:
                return redirect('dashboard_candidate')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirection selon le rôle
            if user.role == 'recruiter':
                return redirect('dashboard_recruiter')
            else:
                return redirect('dashboard_candidate')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page login après logout