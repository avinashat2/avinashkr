from django.urls import path
from . import views




urlpatterns = [
    path('', views.Index, name='index'),
    path('sign-up', views.Signuphandle, name='signup'),
    path('log-in', views.Loginhandle, name='login'),
    path('logout', views.Logouthandle, name='logout'),
    path('add-post', views.Addpost, name='addpost'),
    path('read-post/<int:id>/', views.Readpost, name='readpost'),
    path('comment/<int:id>/', views.CommentView, name='comment'),





]
