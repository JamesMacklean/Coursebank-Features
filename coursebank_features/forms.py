from django import forms
from .models import *

####################### COURSE TAGS #######################
class CommaSeparatedCharField(forms.CharField):
    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',') if item.strip()]
    
class CourseTagForm(forms.ModelForm):
    subtopic = CommaSeparatedCharField(required=False)
    skills = CommaSeparatedCharField(required=False)
    organization = CommaSeparatedCharField(required=False)
    class Meta:
        model = CourseTag
        fields = ['course', 'primary_topic', 'subtopic', 'skills', 'organization']
    
    ############### CommaSeparatedCharField ###############
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subtopic'].widget.attrs['placeholder'] = 'Subtopic 1, Subtopic 2, ...'
        self.fields['skills'].widget.attrs['placeholder'] = 'Skill 1, Skill 2, ...'
        self.fields['organization'].widget.attrs['placeholder'] = 'Organization 1, Organization 2, ...'    

    def clean_subtopic(self):
        data = self.cleaned_data['subtopic']
        if not data:
            return []
        subtopics = []
        for name in data:
            subtopic, _ = SubTopic.objects.get_or_create(name=name)
            subtopics.append(subtopic)
        return subtopics

    def clean_skills(self):
        data = self.cleaned_data['skills']
        if not data:
            return []
        skills = []
        for name in data:
            skill, _ = Skill.objects.get_or_create(name=name)
            skills.append(skill)
        return skills

    def clean_organization(self):
        data = self.cleaned_data['organization']
        if not data:
            return []
        organizations = []
        for name in data:
            organization, _ = Organization.objects.get_or_create(name=name)
            organizations.append(organization)
        return organizations
    
class PrimaryTopicForm(forms.ModelForm):
    primary_topics = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add primary topics separated by commas'}))
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
    subtopics = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add subtopics separated by commas'}))
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
    skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add skills separated by commas'}))
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
    organizations = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add organizations separated by commas'}))
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
