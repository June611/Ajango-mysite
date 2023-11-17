from django.urls import path

from . import views  #from .views import BlogList, BlogDetail, inlcude the boss,  boss.employee

from .views import event_stream

app_name = "qa"

urlpatterns = [
    # ex : /qa/
    path("", views.index, name = "index"),
    path("results/", views.results,  name="results"),
    path("all/", views.ShowallView.as_view(), name = "showall"),
    path('text2json/', views.Text2jsonList.as_view(), name = "text-list"),
    path('text2json/<int:pk>/', views.Text2jsonDetail.as_view(), name = "text-detail"),
    path('event-stream/', event_stream, name='event-stream'),
]
