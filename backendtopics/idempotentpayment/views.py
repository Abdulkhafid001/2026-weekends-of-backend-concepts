from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from rest_framework.views import APIView


def pay(request):
    return render(request, 'payment.html')


def process_payment(request):
    if request.method == 'POST':
        idempotency_key = request.POST.get['idempotentKey']
        return JsonResponse({'status': 'success', 'message': f'payment with has{idempotency_key} come in'})
    return render(request, 'payment.html')
