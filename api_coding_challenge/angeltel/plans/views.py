from rest_framework import viewsets

from angeltel.plans.models import Plan
from angeltel.plans.serializers import PlanSerializer


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer