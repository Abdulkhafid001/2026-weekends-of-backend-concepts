from django.urls import path
from .views import pay, process_payment
urlpatterns = [
    path('pay/', pay),
    path('pay/checkout/', process_payment)

]
