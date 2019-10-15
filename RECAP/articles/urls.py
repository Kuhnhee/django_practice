from django.urls import path
from . import views

app_name = 'articles' # app name 설정

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    path('<int:article_pk>/comments', views.commentCreate, name='commentCreate'),
    path('<int:article_pk>/comments_delete/<int:comment_id>', views.commentDelete, name='commentDelete'),
]