from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry_page, name="entry"),
    path("random", views.random_page, name="random")
]
