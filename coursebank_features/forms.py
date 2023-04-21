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
    primary_topics = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add primary topics separated by commas'}))
    class Meta:
        model = PrimaryTopic
        fields = []
        
    def save(self):
        primary_topic_names = [s.strip() for s in self.cleaned_data['primary_topics'].split(', ')]
        primary_topics = []
        for name in primary_topic_names:
            if name:
                primary_topic, _ = PrimaryTopic.objects.get_or_create(name=name)
                primary_topics.append(primary_topic)
        return primary_topics

class SubTopicForm(forms.ModelForm):
    subtopics = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add subtopics separated by commas'}))
    class Meta:
        model = SubTopic
        fields = []
        
    def save(self):
        subtopic_names = [s.strip() for s in self.cleaned_data['subtopics'].split(', ')]
        subtopics = []
        for name in subtopic_names:
            if name:
                subtopic, _ = SubTopic.objects.get_or_create(name=name)
                subtopics.append(subtopic)
        return subtopics

class SkillForm(forms.ModelForm):
    skills = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add skills separated by commas'}))
    class Meta:
        model = Skill
        fields = []
        
    def save(self):
        skill_names = [s.strip() for s in self.cleaned_data['skills'].split(', ')]
        skills = []
        for name in skill_names:
            if name:
                skill, _ = Skill.objects.get_or_create(name=name)
                skills.append(skill)
        return skills

class OrganizationForm(forms.ModelForm):
    organizations = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add organizations separated by commas'}))
    class Meta:
        model = Organization
        fields = []
        
    def save(self):
        organization_names = [s.strip() for s in self.cleaned_data['organizations'].split(', ')]
        organizations = []
        for name in organization_names:
            if name:
                organization, _ = Organization.objects.get_or_create(name=name)
                organizations.append(organization)
        return organizations
####################### COURSE TAGS #######################
