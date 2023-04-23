from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from coursebank_features.forms import *
from coursebank_features.models import *

# tutor local run lms python -c "from django.conf import settings; print(settings.INSTALLED_APPS)"
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

# Generic View for staff members
@staff_member_required
def staff_view(request, template_name, context):
    if request.user.is_authenticated:
        context['profile'] = request.user
    return render(request, template_name, context)

# Main view for the app
def main(request):
    template_name = 'features/main.html'
    context = {}
    return staff_view(request, template_name, context)

####################### COURSE TAGS #######################
# View course tags
def course_tag(request):
    template_name = 'course_tags/course_tag.html'
    context = {'course_tags': CourseTag.objects.all()}
    return staff_view(request, template_name, context)

# Add tags to a course
def add_course_tag(request):
    template_name = 'course_tags/add_course_tag.html'
    if request.method == 'POST':
        form = CourseTagForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseTagForm()
    else:
        form = CourseTagForm()
    return staff_view(request, template_name, {'form': form})

# Add primary topics
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
    return staff_view(request, template_name, {'form': form, 'primary_topics': primary_topics})

# Add subtopics
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
    return staff_view(request, template_name, {'form': form, 'subtopics': subtopics})

# Add skills
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
    return staff_view(request, template_name, {'form': form, 'skills': skills})

# Add organizations
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
    return staff_view(request, template_name, {'form': form, 'organizations': organizations})
