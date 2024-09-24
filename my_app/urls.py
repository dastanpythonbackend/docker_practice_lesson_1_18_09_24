from django.urls import path
from .views import CarBrandView

urlpatterns = [
    path('', CarBrandView.as_view()),
]
