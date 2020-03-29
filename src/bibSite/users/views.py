from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserResgistrationForm

def register(request):
    if request.method == 'POST':
        form = UserResgistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('bib-home')
    else:
        form = UserResgistrationForm()
    return render(request, 'users/register.html', {'form': form})
