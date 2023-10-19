from django.urls import path
from .views import BrandListView, CarListView, VideoListView, AboutListView, ImageView, FAQListView, \
    TopCarsAPIView, SliderAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TopCarsAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API for Ecopower Project",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)   


urlpatterns = [

    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('cars/', CarListView.as_view(), name='car-list'),
    path('car_detail/', SliderAPIView.as_view(), name='car_detail-list'),
    path('top-cars/', TopCarsAPIView.as_view(), name='top_cars'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('about/', AboutListView.as_view(), name='about-list'),
    path('images/', ImageView.as_view(), name='image-list'),
    path('faq/', FAQListView.as_view(), name='faq-list'),


    path('swagger-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
