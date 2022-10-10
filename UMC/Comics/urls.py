from django.urls import path
from Comics import views

urlpatterns = [
    path('', views.Comics.as_view())
]