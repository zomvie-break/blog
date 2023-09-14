from rest_framework import generics

from api.mixins import UserQuerySetMixin

from .models import Weight
from .serializers import WeightSerializer

import datetime
# apis
class WeightListCreateAPIView(
    UserQuerySetMixin, 
    generics.ListCreateAPIView):
    serializer_class = WeightSerializer
    queryset = Weight.objects.all()
    user_field = 'user'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WeightListSampleAPIView(
    generics.ListAPIView):
    serializer_class = WeightSerializer
    queryset = Weight.objects.filter(user__id="1")

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


class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(request.body)
        # print(request.scheme)
        # print(request.method)
        # print(request.META)

        response = self.get_response(request)

        return response