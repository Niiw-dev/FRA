from django.urls import path
from . import views
from .views import mark_attendance

app_name = 'attendance'

urlpatterns = [
    path('mark/', mark_attendance, name='mark'),
    path('fingerprints/', views.fingerprintList, name='fingerprintList'),
    path('fingerprints/new/', views.fingerprint_create, name='fingerprint_create'),
    path('fingerprints/<int:pk>/edit/', views.fingerprint_update, name='fingerprint_update'),
    path('fingerprints/<int:pk>/delete/', views.fingerprint_delete, name='fingerprint_delete'),
]

