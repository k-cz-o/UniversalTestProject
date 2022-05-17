from django.urls import path
from .views import FileSummary


urlpatterns = [
    path('api/', FileSummary.as_view()),
]