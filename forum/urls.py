from django.urls import path

from forum import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumListView.as_view(), name='forum-list'),
    path('<int:pk>/detail/', views.ForumDetailView.as_view(), name='forum-detail'),
    path('<int:forum_pk>/topic/add/', views.TopicCreateView.as_view(), name='topic-add'),
    path('<int:forum_pk>/topic/<int:topic_pk>/detail/',
         views.TopicDetailView.as_view(), name='topic-detail'),
    path('<int:forum_pk>/topic/<int:topic_pk>/comment/add/',
         views.CommentCreateView.as_view(), name='comment-add'),

]
