from django.shortcuts import render, redirect
from django.contrib.auth import login

from accounts.user import user
from .forms import RegisterForm




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})