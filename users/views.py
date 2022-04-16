from django.shortcuts import redirect, render
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
# def login_view(request):
#     form = UserLoginForm()
#     if (request.method == "POST"):
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(request, username=form.cleaned_data('username'), password=form.cleaned_data('password'))
#             login(request, user)
#             return redirect('home')
            
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)