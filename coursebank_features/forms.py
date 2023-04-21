from django import forms
from .models import *

####################### COURSE TAGS #######################
class CourseTagForm(forms.ModelForm):
    
    subtopic = forms.ModelMultipleChoiceField(queryset=SubTopic.objects.all(), required=False)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), required=False)
    organization = forms.ModelMultipleChoiceField(queryset=Organization.objects.all(), required=False)
    class Meta:
        model = CourseTag
        fields = ['course', 'primary_topic', 'subtopic', 'skills', 'organization']

class PrimaryTopicForm(forms.ModelForm):
    class Meta:
        model = PrimaryTopic
        fields = ['name']
        
class SubTopicForm(forms.ModelForm):
    class Meta:
        model = SubTopic
        fields = ['name']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name']
####################### COURSE TAGS #######################
