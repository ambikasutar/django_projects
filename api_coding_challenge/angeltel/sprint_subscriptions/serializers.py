from rest_framework import serializers
from angeltel.sprint_subscriptions.models import SprintSubscription


class SprintSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SprintSubscription
        fields = '__all__'
