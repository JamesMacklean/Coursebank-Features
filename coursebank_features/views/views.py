from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

from coursebank_features.models import *
from coursebank_features.forms import CourseTagForm

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
def main(request):
    template_name = 'features/main.html'
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
            return redirect('main')
    else:
        form = CourseTagForm()
    
    return render(request, template_name, {'form': form})
####################### COURSE TAGS #######################