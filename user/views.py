from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request, "user/index.html")


def signup(request):
    if request.method == "GET":
        return render(request, "user/signup.html")
    elif request.method == "POST":
        user_id = request.POST["id"]
        if request.POST["pw1"] == request.POST["pw2"]:
            user_pw = request.POST["pw1"]
        else:
            return render(request, "user/signup.html")
        nickname = request.POST["name"]
        add_list = User(username=user_id, nickname=nickname)
        add_list.set_password(user_pw)
        add_list.save()
        return render(request, "user/signup_c.html")


def login(request):
    if request.method == "GET":
        return render(request, "user/login.html")

    elif request.method == "POST":
        user_id = request.POST["id"]
        user_pw = request.POST["pw"]
        index_datas = User.objects.filter(username=user_id)


# authenticate 사용하여 none 인지 확인 >>
