from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def index(request):
    # index_datas = Post.objects.filter(delete=False).order_by("-pub_date")
    # context = {"Post_data" : index_datas}
    print("index 호출")
    return HttpResponse("hello")