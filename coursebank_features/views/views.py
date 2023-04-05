from django.shortcuts import render
from django.contrib.auth.models import User

def dashboard(request):
    template_name = 'features/dashboard.html'
    context = {}

    profile = None

    if request.user.is_authenticated:
        try:
            # uname = User.objects.get(username=request.user)
            context['profile'] = request.user
        except:
            context['profile'] = profile

    context['profile'] = profile
    
    return render(request, template_name, context)
