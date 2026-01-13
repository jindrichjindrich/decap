# pages/urls.py
from django.urls import path
from .views import page

urlpatterns = [
    path("", page, {"slug": "home"}, name="home"),
    path("about/", page, {"slug": "about"}, name="about"),
]