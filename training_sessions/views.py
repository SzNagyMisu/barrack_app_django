from django.shortcuts import render

from .models import TrainingSession

def index(request):
    training_sessions = TrainingSession.objects.all()
    return render(request, "training_sessions/index.html", {"training_sessions": training_sessions})
