from django import forms


from .models import Sensor


class SensorForm(form.ModelForms):

    class Meta:
        model = Sensor
        fields = '__all__'