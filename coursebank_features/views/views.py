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

    if request.user.is_authenticated:
        try:
            # uname = User.objects.get(username=request.user)
            context['profile'] = request.user
        except:
            context['profile'] = None

    
    return render(request, template_name, context)

####################### COURSE TAGS #######################

# FOR VIEWING COURSE TAGS
def course_tag(request):
    template_name = 'course_tags/course_tag.html'
    context = {}
    
    course_tags = CourseTag.objects.all()
    context['course_tags'] = course_tags
    
    return render(request, template_name, context)

# FOR ADDING TAGS ON A COURSE
def add_course_tag(request):
    template_name = 'course_tags/add_course_tag.html'
    
    if request.method == 'POST':
        form = CourseTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_tag')
    else:
        form = CourseTagForm()
    
    return render(request, template_name, {'form': form})

# FOR ADDING PRIMARY TOPICS
def add_primary_topic(request):
    if request.method == 'POST':
        form = PrimaryTopicForm(request.POST)
        if form.is_valid():
            form.save()
            form = PrimaryTopicForm()
    else:
        form = PrimaryTopicForm()

    primary_topics = PrimaryTopic.objects.all()

    return render(request, 'course_tags/add_tag.html', {'form': form, 'tags': primary_topics})

# FOR ADDING SUBTOPICS
def add_subtopic(request):
    if request.method == 'POST':
        form = SubTopicForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubTopicForm()
    else:
        form = SubTopicForm()

    subtopics = SubTopic.objects.all()

    return render(request, 'course_tags/add_tag.html', {'form': form, 'tags': subtopics})

# FOR ADDING SKILLS
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            form = SkillForm()
    else:
        form = SkillForm()

    skills = Skill.objects.all()

    return render(request, 'course_tags/add_tag.html', {'form': form, 'tags': skills})

# FOR ADDING ORGANIZATIONS
def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            form = OrganizationForm()
    else:
        form = OrganizationForm()

    organizations = Organization.objects.all()

    return render(request, 'course_tags/add_tag.html', {'form': form, 'tags': organizations})
####################### COURSE TAGS #######################