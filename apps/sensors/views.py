from django.shortcuts import render
from django.views.generic import ListView

from .models import SensorData


class IndexView(ListView):
    model = SensorData
    template_name = 'sensordata/index.html'
    context_object_name = 'sensordata'
    paginate_by = 20