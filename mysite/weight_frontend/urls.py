from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.WeightIndexView.as_view(), name='weight-sample'),
    path('user/', views.WeightUserView.as_view(), name='weight-user'),
]
