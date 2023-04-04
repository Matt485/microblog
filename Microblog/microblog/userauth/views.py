from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .register import UserCreationForm as CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login

@login_required
def account(request):
    return render(request, 'userauth/account.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/register/register_success')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'userauth/register.html', context)

def register_success(request):
    return render(request, 'userauth/register_success.html')
