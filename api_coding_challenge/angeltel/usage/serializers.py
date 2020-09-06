from rest_framework import serializers
from angeltel.usage.models import DataUsageRecord, VoiceUsageRecord, AllUsageRecord


class DataUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUsageRecord
        fields = '__all__'


class VoiceUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoiceUsageRecord
        fields = '__all__'


class AllUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllUsageRecord
        fields = '__all__'