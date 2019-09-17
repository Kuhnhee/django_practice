from django.urls import path
from . import views

urlpatterns = [
    path('', views.artii),    # '' -> 바깥에서 보면 artii/ 와 동일
    path('result/', views.artiiresult),
]
