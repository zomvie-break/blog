from django.urls import path
from . import views

app_name = "weight-frontend"

urlpatterns = [
    path('sample/', views.WeightIndexView.as_view(), name='weight-sample'),
    path('user/', views.WeightUserView.as_view(), name='weight-user'),
]
