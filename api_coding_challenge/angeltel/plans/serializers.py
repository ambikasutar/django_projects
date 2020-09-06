from rest_framework import serializers

from angeltel.plans.models import Plan


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'