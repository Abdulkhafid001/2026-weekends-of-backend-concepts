from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Payment


def pay(request):
    return render(request, 'payment.html')


def process_payment(request):
    if request.method == 'POST':
        # parse body data from json to use for compute
        frontend_data = json.loads(request.body)
        idempotent_key = frontend_data.get('idempotency_key')
        total = frontend_data.get('total')
        username = frontend_data.get('username')
        # create payment object in DB
        # 1. check if idempotent key coming client has been used for any payment in DB
        try:
            payment_in_db = Payment.objects.get(idempotent_key=idempotent_key)
            # data = {'status': 'true', 'message': 'yuou'}
            return JsonResponse({'message': f'found with payment with key {payment_in_db.idempotent_key} so it is returned'}, safe=False)
        except Payment.DoesNotExist:
            # if payment does not exist create a new payment
            payment = Payment(username=username, idempotent_key=idempotent_key, total=int(total))
            payment.transaction_status = 'Completed'
            payment.save()
            return JsonResponse({'message': f'new payment with key {payment.idempotent_key} created'}, safe=False)
    data = {'message': 'request processed!'}
    return JsonResponse(data, safe=False)
