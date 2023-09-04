from rest_framework import generics

from api.mixins import UserQuerySetMixin

from .models import Weight
from .serializers import WeightSerializer

# apis
class WeightListAPIView(
    UserQuerySetMixin, 
    generics.ListCreateAPIView):
    serializer_class = WeightSerializer
    queryset = Weight.objects.all()

class WeightListSampleAPIView(
    generics.ListAPIView):
    serializer_class = WeightSerializer
    queryset = Weight.objects.filter(user__username="admin")

class WeightDetailAPIView(
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    serializer_class = WeightSerializer
    queryset = Weight.objects.all()

class WeightUpdateAPIView(
    UserQuerySetMixin,
    generics.UpdateAPIView):
    serializer_class= WeightSerializer
    queryset = Weight.objects.all()

class WeightDeleteAPIView(
    UserQuerySetMixin,
    generics.DestroyAPIView):
    serializer_class= WeightSerializer
    queryset = Weight.objects.all()