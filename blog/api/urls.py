from django.urls import path

from .views import APIBlogDetail, APIBlogList

urlpatterns = [
   path('blogs/', APIBlogList.as_view()),
   path('blogs/<int:pk>/', APIBlogDetail.as_view())
]
