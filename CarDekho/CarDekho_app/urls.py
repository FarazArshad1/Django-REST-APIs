from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('showroom',views.Showroom_Viewset, basename = 'showroom')


urlpatterns = [
    path('list',views.car_list_view, name='car_list'),
    path('car/<int:pk>',views.car_detail_view,name='car_detail'),
    path(r'',include(router.urls)),
    # path('showroom',views.Showroom_View.as_view(),name='Showroom views'),
    # path('showroom/<int:pk>',views.Showroom_Details.as_view(),name='Showroom_detail'),
    path('review/<int:pk>', views.ReviewDetail.as_view(),name = 'review_list'),
    path('review',views.ReviewList.as_view(),name = 'review_lists')
]