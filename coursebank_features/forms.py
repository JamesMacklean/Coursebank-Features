from django import forms
from .models import CourseTag

####################### COURSE TAGS #######################
class CourseTagForm(forms.ModelForm):
    class Meta:
        model = CourseTag
        fields = ['course', 'primary_topic', 'subtopic', 'skills', 'organization']
####################### COURSE TAGS #######################
