from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import infoContact
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class PaymentViewSet(viewsets.ModelViewSet):
    # ...existing code...
    pass

@csrf_exempt
def checkout_view(request):
    return render(request, 'checkout.html')
