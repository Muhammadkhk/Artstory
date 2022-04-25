from django.urls import path

from .views import my_profile_page, singin_user, singup_user, singout,edit_user_profile, your_profile_page, your_profile_page1

urlpatterns = [
    path('singin', singin_user, name='singin_user'),
    path('singup', singup_user, name='singup_user'),
    path('singout', singout, name='singout'),
    path('profile', my_profile_page, name='profile'),
    path('editprofile',edit_user_profile, name='editprofile'),
    path('your_profile_page',your_profile_page, name='your_profile_page'),
    path('your_profile_page1',your_profile_page1, name='your_profile_page1'),
    
]