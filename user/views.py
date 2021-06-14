from django.shortcuts import render
from .models import User
from user.forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "user/index.html")


def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["ID"]
            if form.cleaned_data["PW"] == form.cleaned_data["PW_C"]:
                user_pw = form.cleaned_data["PW"]
                nickname = form.cleaned_data["nickname"]
                add_list = User(username=user_id, nickname=nickname)
                add_list.set_password(user_pw)
                add_list.save()
                return render(request, "user/signup_c.html")
        # ERROR
        form = SignupForm()
        return render(request, "user/signup.html", {"form":form})
    else:
        form = SignupForm()
        return render(request, "user/signup.html", {"form":form})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["ID"]
            user_pw = form.cleaned_data["PW"]
            user = authenticate(request, username=user_id, password=user_pw)
            if user_id is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("post:index"))
        # ERROR
        form = LoginForm()
        return render(request, "user/login.html", {"form":form})
    else:
        form = LoginForm()
        return render(request, "user/login.html", {"form":form})

# authenticate 사용하여 none 인지 확인 >>
