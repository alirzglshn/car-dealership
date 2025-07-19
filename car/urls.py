from django.urls import path
from car import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('person' , views.PersonViewSet)

urlpatterns = [
    # path('person-view/' , views.person_view),

    path('car-view/' , views.car_view),
    path('information/' , views.info_view)
]

urlpatterns += router.urls