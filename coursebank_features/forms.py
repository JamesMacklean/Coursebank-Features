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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add primary topic'}),
        }

class SubTopicForm(forms.ModelForm):
    class Meta:
        model = SubTopic
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add subtopic'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add skill'}),
        }

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add organization'}),
        }
####################### COURSE TAGS #######################
