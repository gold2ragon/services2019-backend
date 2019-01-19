from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
# schema_view = get_schema_view(title='Service2019 API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'merchants', views.MerchantViewSet)
router.register(r'businessusers', views.BusinessUserViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'chats', views.ChatViewSet)
router.register(r'carmakes', views.CarMakeViewSet)
router.register(r'carmodels', views.CarModelViewSet)
router.register(r'carfuels', views.CarFuelViewSet)
router.register(r'cartransimissions', views.CarTransmissionViewSet)
router.register(r'carlists', views.CarListViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'servicelists', views.ServiceListViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'servicehistorys', views.ServiceHistoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]