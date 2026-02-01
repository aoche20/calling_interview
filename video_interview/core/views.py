from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_recruiter_view(request):
    return render(request, 'core/dashboard_recruiter.html')

@login_required
def dashboard_candidate_view(request):
    return render(request, 'core/dashboard_candidate.html')
