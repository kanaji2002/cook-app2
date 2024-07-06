from django.urls import path
from . import views
app_name='photo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreatePhotoView.as_view(),name='post'),
    path('post/done/',views.PostSuccessView.as_view(),name='post_done'),
]

