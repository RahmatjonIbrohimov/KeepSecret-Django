from django.urls import path

from . import views

urlpatterns = [
    path('', views.Tweet_List, name='tweet_list'),
    path('salom/', views.home, name='home'),
    path('add_tweet/', views.Add_Tweet, name='add_tweet'),
    path('add_comment/<int:tweet_id>/', views.Add_Comment, name='add_comment'), 
    path('like/<int:pk>/', views.LikeView, name='like_tweet'),
    path('hashtag/<str:hashtag>/', views.HashtagView, name='hashtag_view'),
    path('quests/', views.AllTweetsView, name='all_tweets'),
    path('search/', views.SearchViews, name='search-view'),
]
