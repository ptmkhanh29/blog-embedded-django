from django.urls import path
from . import views
from .views import CategoryView

app_name = 'blog'

urlpatterns = [
    # post views
    #path('', views.post_list, name='post_list'),
    path('', views.post_list, name='home'),
    path('blog/', views.PostListViewBlog.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('category/<slug:slug>/', views.post_list, name='category-detail'),
]
