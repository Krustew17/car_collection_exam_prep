from django.urls import path, include

from carcollection.car.views import CarDetails, CreateCar, EditCar, DeleteCar

urlpatterns = (
    path('create/', CreateCar.as_view(), name='create car'),
    path('<int:pk>/', include([
        path('delete/', DeleteCar.as_view(), name='delete car'),
        path('edit/', EditCar.as_view(), name='edit car'),
        path('details/', CarDetails.as_view(), name='details car'),
    ])),
)
