from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User
from django.urls import reverse


# Create your views here.
def index(request):
    index_datas = Post.objects.filter(delete=False).order_by("-pub_date")
    context = {"Post_data": index_datas}
    return render(request, "post/index.html", context)


def add(request):
    if request.method == "GET":
        return render(request, "post/add.html")
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        writer = User.objects.get(pk=1)
        files = request.FILES["files"]
        # files = request.FILES.get("files", '')
        print(files)
        add_list = Post(title=title, content=content, writer=writer, files=files)
        add_list.save()
        return HttpResponseRedirect(reverse("post:index"))

def detail(request, post_id):
    if request.method == "GET":
        try:
            id_data = Post.objects.get(pk=do_list_id)
        except Do_list.DoesNotExist:
            raise Http404("없거나 삭제된 게시물입니다.")
        context = {"id_data": id_data}
        return render(request, "post/detail.html", context)
    elif request.method == "POST":
        id_data = Post.objects.get(pk=do_list_id)
        id_data.delete = True
        id_data.save()
        return HttpResponseRedirect(reverse("post:index"))

def edit(request, post_id):
    if request.method == "GET":
        try:
            id_data = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404("없거나 삭제된 게시물입니다.")
        context = {"id_data": id_data}
        return render(request, "post/edit.html", context)
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        files = request.FILES["files"]
        id_data = Post.objects.get(pk=post_id)
        id_data.title = title
        id_data.content = content
        id_data.files = files
        id_data.modify_date = timezone.now()
        id_data.save()
        return HttpResponseRedirect(reverse("post:index"))