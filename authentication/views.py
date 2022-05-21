from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import View

from authentication import forms

class LoginPage(View):

  form_class = forms.LoginFrom
  template_name = 'authentication/login.html'

  def get(self, request):
    message = ''
    return render(request, self.template_name, context={
              'form': self.form_class(),
              'message': message
            })

  def post(self, request):
    form = self.form_class(request.POST)
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
    return render(request, self.template_name, context={
              'form': form,
              'message': message
            })


def logout_user(request):
  logout(request)
  return redirect('login')
