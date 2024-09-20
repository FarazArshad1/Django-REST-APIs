from django.urls import path
from . import views

urlpatterns = [
    path('list',views.car_list_view, name='car_lis'),
    path('<int:pk>',views.car_detail_view,name='car_detail'),
    path('showroom',views.Showroom_View.as_view(),name='Showroom views')
]