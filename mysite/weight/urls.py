from django.urls import path
from . import views

urlpatterns = [
    # apis
    path('', views.WeightListCreateAPIView.as_view(), name='weight-list-api'),
    path('<int:pk>/', views.WeightDetailAPIView.as_view(), name='weight-detail-api'),
    path('<int:pk>/update/', views.WeightUpdateAPIView.as_view(), name='weight-update-api'),
    path('<int:pk>/delete/', views.WeightDeleteAPIView.as_view(), name='weight-delete-api'),
    
    # sample
    path('sample/', views.WeightListSampleAPIView.as_view(), name='weight-sample-api'),
    
    
]
