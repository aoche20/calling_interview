from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from interviews.models import Interview

@login_required
def dashboard_recruiter_view(request):
    interviews = Interview.objects.filter(recruiter=request.user)
    return render(request, 'core/dashboard_recruiter.html', {'interviews': interviews})

@login_required
def dashboard_candidate_view(request):
    interviews = Interview.objects.filter(candidate=request.user)
    return render(request, 'core/dashboard_candidate.html', {'interviews': interviews})
