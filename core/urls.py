from django.urls import path
from .views import BusinessViewSet
from . import views

urlpatterns = [
    path("businesses/", BusinessViewSet.as_view({'post': 'create'}), name="generate-landing-page"),
    path('generate_post/', views.generate_post),
]