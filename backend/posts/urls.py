"""
Urls for Posts model
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('create/', views.PostCreate.as_view(), name='create_post'),

    path('docs/', views.DocumentCreate.as_view(), name='create_doc'),
    path('docs/all/', views.DocumentListView.as_view(), name='list_doc'),
    path('random/', views.random_nubers, name='random_numbers'),
]
