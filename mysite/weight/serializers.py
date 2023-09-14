from django.utils import timezone
from rest_framework import serializers
from .models import Weight
import datetime

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class WeightSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Weight
        fields = [
            'pk',
            'owner',
            'mass',
            'created',
        ]

    def create(self, validated_data):

        created = validated_data.pop('created', None)

        if created == None:
            created = timezone.now()
        return Weight.objects.create(created=created, **validated_data)
        