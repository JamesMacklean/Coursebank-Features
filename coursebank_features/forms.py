from django import forms
from .models import CourseTag

class CourseTagForm(forms.ModelForm):
    class Meta:
        model = CourseTag
        fields = ['course', 'primary_topic', 'subtopic', 'skills', 'organization']
