from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

from coursebank_features.api.serializers import *
from coursebank_features.api.variables import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.content.learning_sequences.models import LearningContext

class CoursesAPIView(APIView):
    def get(self, request):
        try:
            # Get all course overviews
            course_overviews = CourseOverview.objects.exclude(id__in=EXCLUDED_COURSES)
            
            # Get enrollment counts for each course
            course_data = []
            for course_overview in course_overviews:                    
                enrollment_end = course_overview.enrollment_end
                if enrollment_end is None or enrollment_end > timezone.now():
                    enrollment_count = CourseEnrollment.objects.filter(
                        course_id=course_overview.id,
                        is_active=True
                    ).count()
                    
                    course_info = {
                        'course_id': course_overview.id,
                        'course_name': course_overview.display_name,
                    }
                    
                    learning_context = LearningContext.objects.get(context_key=course_overview.id)

                    if learning_context:
                        course_info['date_published'] = learning_context.published_at
                    else:
                        course_info['date_published'] = ''
                        
                    enrolled_in_honor = CourseEnrollment.objects.filter(
                        course_id=course_overview.id,
                        is_active=True,
                        mode='honor'
                    ).exists()
                    
                    if enrolled_in_honor:
                        course_info['mode'] = 'honor'
                    else:
                        course_info['mode'] = ''
                        
                    # Add enrollment_count key to course_info dictionary
                    course_info['enrollment_count'] = enrollment_count
                    
                    course_data.append(course_info)
                    
            # Sort the course_data list by enrollment count in descending order
            sorted_enrollments = sorted(course_data, key=lambda x: x['enrollment_count'], reverse=True)

            # Serialize the enrollment data
            serializer = CoursesSerializer(sorted_enrollments, many=True)

            # Return the enrollment data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        
# class CourseBundleListAPIView(APIView):
#     def get(self, request):
#         bundles = CourseBundle.objects.all()
#         serializer = CourseBundleSerializer(bundles, many=True)
#         return Response(serializer.data)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
