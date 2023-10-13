from django.urls import path

from . import views

app_name = "qa"

urlpatterns = [
    # ex : /qa/
    path("", views.index, name = "index"),

]
