from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 下記のURLは全てログイン必須。
    path('post/new/', views.post_new, name='post_new'),
    path('post/new/draftsave/', views.post_new_draft_save, name='post_new_draft_save'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/edit/draftsave/',views.post_edit_draft_save, name='post_edit_draft_save'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
