from django.shortcuts import render

def monitor_view(request):
    return render(request, 'monitor/cliente.html')
