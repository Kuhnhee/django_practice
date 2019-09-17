from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one),    # '' -> 바깥에서 보면 artii/ 와 동일
    path('two/', views.two),
]