from django.urls import path


from .views import CarsList, CarsDetail

urlpatterns = [

    path('', CarsList.as_view(), name='cars_list'),

    path('<int:pk>/', CarsDetail.as_view(), name='cars_detail'),
]