from django.urls import path
from employee import views


urlpatterns = [
     path('post-employee/' , views.post_employee ) ,
     path('get-employee/' , views.list_employees ),
     path('get-update-delete-employee/<int:pk>' , views.get_update_delete_employee ),

]