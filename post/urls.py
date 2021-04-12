from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("detail/<int:do_list_id>/", views.detail, name="detail"),
    path("edit/<int:do_list_id>/", views.edit, name="edit"),
]
