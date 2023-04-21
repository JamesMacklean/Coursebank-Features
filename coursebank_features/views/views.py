from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

from coursebank_features.models import *
from coursebank_features.forms import *
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
    context['course_tags'] = course_tags
    
    return render(request, template_name, context)

####################### COURSE TAGS #######################
@user_passes_test(lambda u: u.is_staff)
@staff_member_required
class CourseTagCreateView(CreateView):
    model = CourseTag
    form_class = CourseTagForm
    template_name = 'course_tags/add_course_tag.html'
    success_url = reverse_lazy('main')
    
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

def add_primary_topic(request):
    if request.method == 'POST':
        form = PrimaryTopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course_tag')
    else:
        form = PrimaryTopicForm()
    return render(request, 'course_tags/add_primary_topic.html', {'form': form})

def add_subtopic(request):
    if request.method == 'POST':
        form = SubTopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course_tag')
    else:
        form = SubTopicForm()
    return render(request, 'course_tags/add_subtopic.html', {'form': form})

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course_tag')
    else:
        form = SkillForm()
    return render(request, 'course_tags/add_skill.html', {'form': form})

def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course_tag')
    else:
        form = OrganizationForm()
    return render(request, 'course_tags/add_organization.html', {'form': form})
####################### COURSE TAGS #######################