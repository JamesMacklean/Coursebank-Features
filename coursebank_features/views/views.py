from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from coursebank_features.models import *
from coursebank_features.forms import *

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
@staff_member_required
def course_tag(request):
    template_name = 'course_tags/course_tag.html'
    context = {}
    
    course_tags = CourseTag.objects.all()
    context['course_tags'] = course_tags
    
    return render(request, template_name, context)

# FOR ADDING TAGS ON A COURSE
@staff_member_required
def add_course_tag(request):
    template_name = 'course_tags/add_course_tag.html'
    
    if request.method == 'POST':
        form = CourseTagForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseTagForm()
    else:
        form = CourseTagForm()
    
    return render(request, template_name, {'form': form})

# FOR ADDING PRIMARY TOPICS
@staff_member_required
def add_primary_topic(request):
    template_name = 'course_tags/add_primary_topic.html'
    if request.method == 'POST':
        form = PrimaryTopicForm(request.POST)
        if form.is_valid():
            primary_topics = form.save()
            messages.success(request, f"Added primary topics: {', '.join(str(s) for s in primary_topics)}")
            form = PrimaryTopicForm()
    else:
        form = PrimaryTopicForm()

    primary_topics = PrimaryTopic.objects.all()

    return render(request, template_name, {'form': form, 'primary_topics': primary_topics})

# FOR ADDING SUBTOPICS
@staff_member_required
def add_subtopic(request):
    template_name = 'course_tags/add_subtopic.html'
    if request.method == 'POST':
        form = SubTopicForm(request.POST)
        if form.is_valid():
            subtopics = form.save()
            messages.success(request, f"Added subtopics: {', '.join(str(s) for s in subtopics)}")
            form = SubTopicForm()
    else:
        form = SubTopicForm()

    subtopics = SubTopic.objects.all()

    return render(request, template_name, {'form': form, 'subtopics': subtopics})

# FOR ADDING SKILLS
@staff_member_required
def add_skill(request):
    template_name = 'course_tags/add_skill.html'
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skills = form.save()
            messages.success(request, f"Added skills: {', '.join(str(s) for s in skills)}")
            form = SkillForm()
    else:
        form = SkillForm()

    skills = Skill.objects.all()

    return render(request, template_name, {'form': form, 'skills': skills})

# FOR ADDING ORGANIZATIONS
@staff_member_required
def add_organization(request):
    template_name = 'course_tags/add_organization.html'
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organizations = form.save()
            messages.success(request, f"Added organizations: {', '.join(str(s) for s in organizations)}")
            form = OrganizationForm()
    else:
        form = OrganizationForm()

    organizations = Organization.objects.all()

    return render(request, template_name, {'form': form, 'organizations': organizations})