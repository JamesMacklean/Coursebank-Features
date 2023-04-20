from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from models import *

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
def dashboard(request):
    template_name = 'features/dashboard.html'

    profile = None
    if request.user.is_authenticated:
        try:
            # uname = User.objects.get(username=request.user)
            context['profile'] = request.user
        except:
            context['profile'] = profile

    course_tags = CourseTag.objects.all()
    course_display_names = {}
    for course_tag in course_tags:
        course_display_names[course_tag.course.id] = course_tag.course.display_name
    context = {
        'course_tags': course_tags,
        'course_display_names': course_display_names
    }
    
    return render(request, template_name, context)

####################### COURSE TAGS #######################
@user_passes_test(lambda u: u.is_staff)
@staff_member_required
class SubtopicCreateView(CreateView):
    model = SubTopic
    fields = ['name']
    template_name = 'course_tags/create_form.html'
    success_url = reverse_lazy('create_subtopic')

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
class PrimaryTopicCreateView(CreateView):
    model = PrimaryTopic
    fields = ['name']
    template_name = 'course_tags/create_form.html'
    success_url = reverse_lazy('create_primarytopic')

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
class SkillCreateView(CreateView):
    model = Skill
    fields = ['name']
    template_name = 'course_tags/create_form.html'
    success_url = reverse_lazy('create_skill')

@user_passes_test(lambda u: u.is_staff)
@staff_member_required
class OrganizationCreateView(CreateView):
    model = Organization
    fields = ['name']
    template_name = 'course_tags/create_form.html'
    success_url = reverse_lazy('create_organization')
####################### COURSE TAGS #######################