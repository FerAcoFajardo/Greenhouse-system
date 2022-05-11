from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import SensorData, Sensor
from .forms import SensorForm

class IndexView(ListView):
    model = SensorData
    template_name = 'sensordata/index.html'
    context_object_name = 'sensordata'
    paginate_by = 20


class CreateView(CreateView):
    model = Sensor
    template_name = 'sensors/create.html'
    form_class = SensorForm
    success_url = reverse_lazy('sensors:index')