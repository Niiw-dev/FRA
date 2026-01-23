from django.conf import settings
from django.db import models


class Attendance(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attendances'
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    device_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Equipo desde el que se registró la asistencia"
    )

    def __str__(self):
        return f"{self.user} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
