from django.urls import path
from . import views
from .api import views as api_views

app_name = 'sensors'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', api_views.SensorDataCreareAPIView.as_view(), name='api-create'),
]