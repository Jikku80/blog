from django.urls import path
from .import views
from .views import PostListView, SearchResultsListView

from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # path('', PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
]
