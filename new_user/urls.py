from django.urls import path
from new_user import views

urlpatterns = [
    path('post-user/' , views.create_user ),
    path('profile/' , views.user_profile )
]