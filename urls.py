from django.urls import path
from myapp.views import hello
from myapp.views import hi

urlpatterns = [
    path('hello/', hello),
    path('hi/', hi)
]