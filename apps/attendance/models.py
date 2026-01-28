from django.conf import settings
from django.db import models


class Attendance(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attendances'
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class Fingerprint(models.Model):
    fingerprint_uid = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="UID de la huella"
    )
    full_name = models.CharField(
        max_length=150,
        verbose_name="Nombre completo"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name
