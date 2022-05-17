from django.urls import path
from .views import FileSummary, home


urlpatterns = [
    path('api/', FileSummary.as_view()),
    path('home/', home, name="home")
]