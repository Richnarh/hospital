from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages

from account.forms import loginForm
from stu.models import SetupPassword


# def login(request):
#     if request.method == 'POST':
#         form = loginForm(request.POST)
#         if form.is_valid():
#             obj = form.cleaned_data
#             staff_id = obj['staff_id']
#             password = obj['password']
#
#             if (SetupPassword.objects.filter(staff_id=staff_id).exists()
#                     and SetupPassword.objects.filter(password=password).exists()):
#                 staff = authenticate(staff_id=staff_id, password=password)
#                 # login(staff)
#                 return redirect('stu')
#             else:
#                 messages.info(request, 'Incorrect username or password')
#                 return redirect('login')
#         form = loginForm()
#         return render(request, 'login.html', {'form': form})
#     else:
#         form = loginForm()
#         # return render(request, 'login.html', {'form': form})


# def logout_view(request):
#     auth.logout(request)
#     return redirect('/')
