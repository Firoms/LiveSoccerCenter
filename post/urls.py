from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD
    path("add", views.add, name="add"),
=======
>>>>>>> 8fb7be55e2233ebc996a9214624fb21724f8c6c6
]
