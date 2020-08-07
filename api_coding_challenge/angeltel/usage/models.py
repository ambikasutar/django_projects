from django.db import models

from angeltel.att_subscriptions.models import ATTSubscription
from angeltel.sprint_subscriptions.models import SprintSubscription


class DataUsageRecord(models.Model):
    """Raw data usage record for a subscription"""
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateTimeField(null=True)
    kilobytes_used = models.IntegerField(null=False)


class VoiceUsageRecord(models.Model):
    """Raw voice usage record for a subscription"""
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateTimeField(null=True)
    seconds_used = models.IntegerField(null=False)



class AllUsageRecord(models.Model):
    #att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    #sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    #voice_usage_id = models.ForeignKey(VoiceUsageRecord, null=True, on_delete=models.PROTECT)
    data_usage_id = models.ForeignKey(DataUsageRecord, null=True, on_delete=models.PROTECT)