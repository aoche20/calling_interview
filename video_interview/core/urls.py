from django.urls import path
from .views import dashboard_candidate_view, dashboard_recruiter_view




urlpatterns = [
path('dashboard/recruiter/', dashboard_recruiter_view, name='dashboard_recruiter'),
    path('dashboard/candidate/', dashboard_candidate_view, name='dashboard_candidate'),
]