
from . import views
from django.urls import path

urlpatterns = [
    path('blogposts/',views.BlogosPostListCreate.as_view(),name='blogpost-view-create'),
    path('blogposts/<int:pk>/',views.BlogPostRetrieveUpdateDestroy.as_view(),name='update'),
    path('',views.home,name='home')
]
