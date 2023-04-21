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

####################### COURSE TAGS #######################
