from rest_framework import viewsets

from angeltel.purchases.models import Purchase
from angeltel.purchases.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
