from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<int:pk>/', views.PostView.as_view(), name='detail'),
    path(r'archive/', views.archives, name='archives_page'),
    path(r'archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives'),
    path(r'category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path(r'tag/<int:pk>/', views.TagView.as_view(), name='tag'),
]