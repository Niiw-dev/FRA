from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Fingerprint, Attendance
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FingerprintForm


@csrf_exempt
def mark_attendance(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    uid = request.POST.get('fingerprint_uid')

    if not uid:
        return JsonResponse({'error': 'UID requerido'}, status=400)

    try:
        fingerprint = Fingerprint.objects.get(
            fingerprint_uid=uid,
            is_active=True
        )
    except Fingerprint.DoesNotExist:
        # ❌ No existe o está desactivada → NO registrar
        return JsonResponse({
            'success': False,
            'message': 'Huella no autorizada'
        }, status=403)

    last = Attendance.objects.filter(
        fingerprint=fingerprint
    ).order_by('-timestamp').first()

    if last and timezone.now() - last.timestamp < timedelta(hours=1, minutes=45):
        return JsonResponse({
            'success': False,
            'message': 'Asistencia ya registrada recientemente'
        }, status=429)

    Attendance.objects.create(
        fingerprint=fingerprint,
        status='OK'
    )

    return JsonResponse({
        'success': True,
        'name': fingerprint.full_name
    })


@login_required
def fingerprintList(request):
    fingerprints = Fingerprint.objects.all()
    form = FingerprintForm()
    return render(request, 'attendance/fingerprintList.html', {
        'fingerprints': fingerprints,
        'form': form,
        'title': 'Nueva huella'
    })

@login_required
def fingerprint_create(request):
    if request.method == 'POST':
        form = FingerprintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fingerprintList')
    else:
        form = FingerprintForm()

    return render(request, 'attendance/fingerprintForm.html', {
        'form': form,
        'title': 'Nueva huella'
    })

@login_required
def fingerprint_update(request, pk):
    fingerprint = get_object_or_404(Fingerprint, pk=pk)

    if request.method == 'POST':
        form = FingerprintForm(request.POST, instance=fingerprint)
        if form.is_valid():
            form.save()
            return redirect('fingerprintList')
    else:
        form = FingerprintForm(instance=fingerprint)

    return render(request, 'attendance/fingerprintForm.html', {
        'form': form,
        'title': 'Editar huella'
    })

@login_required
def fingerprint_delete(request, pk):
    fingerprint = get_object_or_404(Fingerprint, pk=pk)
    fingerprint.delete()
    return redirect('fingerprintList')

