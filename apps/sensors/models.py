from django.db import models


# Model for animals
class Sensor(models.Model):
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


    class Meta:
        db_table = 'sensors'
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"
        ordering = ['id']

    def __str__(self):
        return f'Sensor name: {self.name} - Sensor type: {self.type}'


class SensorData(models.Model):
    data = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sensors_data'
        verbose_name = "Sensor Data"
        verbose_name_plural = "Sensors Data"
        ordering = ['date']

    def __str__(self):
        return f'Sensor data: {self.data} - Sensor: {self.sensor} - Date: {self.date}'