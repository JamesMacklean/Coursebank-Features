from django.shortcuts import render

def dashboard(request):
    return render(request, 'coursebank_features/dashboard.html')
