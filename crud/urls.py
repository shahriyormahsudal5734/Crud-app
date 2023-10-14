from .views import *
from django.urls import path

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/',user_logout, name='logout'),
    path('addprofile/',User_profile.as_view(), name='addprofile'),
    path('postcreate/',Postcreate.as_view(), name='postcreate'),
    path('editprofile/<int:pk>/',Profile_edit.as_view(), name='editprofile'),
    path('post_edit/<int:pk>/',Post_edit.as_view(), name='post_edit'),
    path('users/<str:username>/',profile_view, name='profile_view'),
    path('delete_post/<int:id>/',delete_post, name='profile_view'),

]