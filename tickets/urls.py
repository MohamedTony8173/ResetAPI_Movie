from django.urls import path 
from .views import GuestViewSerializer,GuestUpdateDeleteView

urlpatterns = [
    path('',GuestViewSerializer.as_view()),
    path('<int:pk>/',GuestUpdateDeleteView.as_view()),
    
]