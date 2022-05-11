from django import forms


from .models import Sensor


class SensorForm(forms.ModelForms):

    class Meta:
        model = Sensor
        fields = '__all__'