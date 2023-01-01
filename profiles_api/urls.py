from django.urls import path
from . import views
urlpatterns = [
    path("hello-view/", views.HelloAppView.as_view()),
]