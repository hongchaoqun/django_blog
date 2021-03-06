from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.clean_data
            user = authenticate(username=cd['username'], password=cd["password"])
            if user:
                login(request, user)
                return HttpResponse("wellcom")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        form = LoginForm()
        return render("account/login.html")
