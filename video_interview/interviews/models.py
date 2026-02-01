from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # Chaîne vers User custom

class Room(models.Model):
    """
    Une salle virtuelle pour un entretien.
    """
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Interview(models.Model):
    """
    Entretien entre un recruteur et un candidat.
    """
    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('scheduled', 'Planifié'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recruiter_interviews',
        limit_choices_to={'role': 'recruiter'}
    )
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_interviews',
        limit_choices_to={'role': 'candidate'}
    )
    room = models.OneToOneField(
        Room,
        on_delete=models.CASCADE,
        related_name='interview',
        null=True,
        blank=True
    )
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.recruiter.username} → {self.candidate.username})"
