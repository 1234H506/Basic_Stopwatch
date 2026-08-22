from django.http import JsonResponse
from django.shortcuts import render
from .models import Timer
from django.utils import timezone


# Create your views here.
def show_index(request):
    return render(request, 'timer/main.html')

def start(request):
    if request.method == 'POST':
        timer = Timer.objects.create(start=timezone.now())
        return JsonResponse({'id':timer.id, 'start': timer.start })
    else:
        return JsonResponse({'message': 'method not allowed'}, status=405)