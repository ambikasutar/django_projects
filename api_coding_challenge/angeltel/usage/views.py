from angeltel.usage.models import DataUsageRecord, VoiceUsageRecord, AllUsageRecord
from django.http import HttpResponse
from rest_framework import viewsets
from angeltel.usage.serializers import DataUsageRecordSerializer, VoiceUsageRecordSerializer, AllUsageRecordSerializer


class DataUsageRecordViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = DataUsageRecord.objects.all()
    serializer_class = DataUsageRecordSerializer


class VoiceUsageRecordViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = VoiceUsageRecord.objects.all()
    serializer_class = VoiceUsageRecordSerializer


class AllUsageRecordViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = AllUsageRecord.objects.all()
    serializer_class = AllUsageRecordSerializer