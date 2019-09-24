from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/answers_create/', views.answers_create, name='answers_create'),
    path('<int:pk>/answers_delete/', views.answers_delete, name='answers_delete'),
    path('random/',views.random, name='random'),
    path('clean/', views.clean, name='clean')
]