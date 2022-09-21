from django.urls import path
from .views import SensorsView, SensorDetailView, MeasurementView, MeasurementDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    # path('sensorupdate/<int:pk>/', SensorUpdateView.as_view()),
    # path('measurement/<pk>', MeasurementView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurementsdetail/', MeasurementDetailView.as_view()),
]
