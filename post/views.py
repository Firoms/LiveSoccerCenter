from post.forms import AddForm
from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
from user.models import User
from django.urls import reverse
from .forms import AddForm
from django.utils import timezone

# Create your views here.
def index(request):
    index_datas = Post.objects.filter(delete=False).order_by("-pub_date")
    context = {"Post_data": index_datas}
    return render(request, "post/index.html", context)


def add(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            writer = User.objects.get(pk=1)
            # files = request.FILES["files"]
            # files = request.FILES.get("files", "")
            files = form.cleaned_data['files']
            add_list = Post(title=title, content=content, writer=writer, files=files)
            add_list.save()
            return HttpResponseRedirect(reverse("post:index"))
    else:
        form = AddForm()
    return render(request, "post/add.html", {'form':form})


def detail(request, post_id):
    if request.method == "GET":
        try:
            id_data = Post.objects.get(pk=post_id)
            context = {"id_data": id_data}
            try:
                comment_datas = Comment.objects.filter(post=post_id, delete=False)
                context["comment_datas"] = comment_datas
            except Comment.DoesNotExist:
                context["comment_data"] = "작성된 댓글이 없습니다."
        except Post.DoesNotExist:
            raise Http404("없거나 삭제된 게시물입니다.")
        return render(request, "post/detail.html", context)
    elif request.method == "POST":
        id_data = Post.objects.get(pk=post_id)
        id_data.delete = True
        id_data.save()
        return HttpResponseRedirect(reverse("post:index"))


def edit(request, post_id):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        print(form)
        print("111")
        if form.is_valid():
            print("222")
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            files = form.cleaned_data["files"]
            print(files)
            id_data = Post.objects.get(pk=post_id)
            id_data.title = title
            id_data.content = content
            id_data.files = files
            id_data.modify_date = timezone.now()
            id_data.save()
            return HttpResponseRedirect(reverse("post:index"))
    else:
        try:
            id_data = Post.objects.get(pk=post_id)
            # form.initial['title'] = id_data.title
            # form.initial['content'] = id_data.content
            # form.initial['files'] = id_data.files
            form = AddForm(instance=id_data)
        except Post.DoesNotExist:
            raise Http404("없거나 삭제된 게시물입니다.")

        context = {"id_data": id_data, "form":form}
        return render(request, "post/edit.html", context)

    print("333")
    return render(request, "post/edit.html", {"form":form})

def comment(request, post_id):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        content = request.POST["comment"]
        post = Post.objects.get(pk=post_id)
        writer = User.objects.get(pk=1)
        add_list = Comment(content=content, post=post, writer=writer)
        add_list.save()
        return HttpResponseRedirect(reverse("post:detail", args=(post_id,)))
