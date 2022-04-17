from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])

            login(request, new_user)
            messages.add_message(request, messages.SUCCESS, f"Account for { new_user.username } has been created🥳")
            # username = form.cleaned_data.get('username')

            # This is definitely not a url that should be used
            return redirect("home")
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)