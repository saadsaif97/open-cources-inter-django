from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from authentication import forms

def logout_user(request):
  logout(request)
  return redirect('login')

def login_page(request):
  message = ''
  form = forms.LoginFrom()
  if request.method == 'POST':
    form = forms.LoginFrom(request.POST)
    if form.is_valid():
      user = authenticate(
        username=form.cleaned_data['username'], 
        password=form.cleaned_data['password'])
      if user is not None:
        login(request, user)
        message = f"You are logged in as {user.username}"
        return redirect('home')
      else:
        message = f"Login failed!"
  return render(request, 'authentication/login.html', context={
    'form': form,
    'message': message
  })
