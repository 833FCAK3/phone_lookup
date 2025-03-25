from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search-phone/", views.search_phone, name="search_phone"),
]
