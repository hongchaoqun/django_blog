from django import forms


class LoginForm(form.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
