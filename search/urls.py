from django.urls import path
from .views import ProfessorSearchView

urlpatterns = [
    path('search/', ProfessorSearchView.as_view(), name='search'),
]
