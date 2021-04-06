from django.shortcuts import render
from .models import Post
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User
from django.urls import reverse
=======
from django.http import HttpResponse
>>>>>>> 8fb7be55e2233ebc996a9214624fb21724f8c6c6


# Create your views here.
def index(request):
<<<<<<< HEAD
    index_datas = Post.objects.filter(delete=False).order_by("-pub_date")
    context = {"Post_data" : index_datas}
    return render(request, "post/index.html", context)

def add(request):
    if request.method == "GET":
        return render(request, "post/add.html")
    elif request.method == "POST":
        writer = User.objects.get(pk=1)
        title = request.POST["title"]
        content = request.POST["content"]
        files = request.FILES["files"]
        # files = request.FILES.get("files", '')
        print(files)
        add_list = Post(
            title=title, content=content, writer=writer, files=files
        )
        add_list.save()
        return HttpResponseRedirect(reverse("post:index"))
=======
    # index_datas = Post.objects.filter(delete=False).order_by("-pub_date")
    # context = {"Post_data" : index_datas}
    print("index 호출")
    return HttpResponse("hello")
>>>>>>> 8fb7be55e2233ebc996a9214624fb21724f8c6c6
