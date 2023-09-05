from django.urls import include, path

urlpatterns = [
    path('weight/', include('weight.urls')),
]
