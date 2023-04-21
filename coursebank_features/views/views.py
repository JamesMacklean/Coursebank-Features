from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from coursebank_features.models import *
from coursebank_features.forms import CourseTagForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
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

    course_tags = CourseTag.objects.all()

    context = {
        'course_tags': course_tags,
    }
    
    return render(request, template_name, context)

####################### COURSE TAGS #######################
@user_passes_test(lambda u: u.is_staff)
@staff_member_required
def add_course_tag(request):
    template_name = 'course_tags/add_course_tag.html'
    
    if request.method == 'POST':
        form = CourseTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseTagForm()
    
    return render(request, template_name, {'form': form})
####################### COURSE TAGS #######################