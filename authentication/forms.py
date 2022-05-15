from django import forms


class LoginFrom(forms.Form):
  username = forms.CharField(max_length=63)
  password = forms.CharField(max_length=63, widget=forms.PasswordInput)
