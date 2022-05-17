from django.urls import path
from .views import FileSummary


urlpatterns = [
    path('api/', FileSummary.as_view()),
    path('home/', "Welcome to Unversal Test Project")
]