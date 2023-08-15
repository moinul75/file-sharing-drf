from django.urls import path 
from .views import HandleFileUpload,home,download

urlpatterns = [
    path('',home,name="home"),
    path('upload/',HandleFileUpload.as_view(),name='upload'),
    path('dwonload/<uid>/', download,)
]

