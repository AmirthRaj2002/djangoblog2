from django.urls import path
from . import views
app_name='meetups'
urlpatterns=[
    path('',views.index,name='home'),
    path('<slug:post>/',views.post_single,name='post_single'),
]