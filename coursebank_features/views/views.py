from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from coursebank_features.models import *

from opaque_keys.edx.keys import CourseKey
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

@staff_member_required
def staff_view(request, template_name, context):
    if request.user.is_authenticated:
        context['profile'] = request.user
    return render(request, template_name, context)

####################### COURSE BUNDLES ################

# def bundles(request,slug):
#     template_name = 'course_bundles/course_bundles.html'
#     context = {}

#     bundle = CourseBundle.objects.get(slug=slug)
#     special_courses = SpecialCourse.objects.filter(is_active=True).filter(course_bundle=bundle)
#     courses = []
#     for special_course in special_courses:
#         course = {'special_course':special_course}
#         course_key = CourseKey.from_string(special_course.course_id)
#         courseoverview = CourseOverview.get_from_id(course_key)
#         course['courseoverview'] = courseoverview
#         courses.append(course)

#     context['courses'] = courses
#     context['bundle'] = bundle
#     return render(request, template_name, context)

####################### PARTNERS ######################

def PartnersCatalogView(request):
    """ renders all partners in main partners page """
    link_partners = []
    for course in PartnerCourse.objects.all():
        if course.partner not in link_partners:
            link_partners.append(course.partner)
    partners = Partner.objects.filter(is_active=True).order_by('-ranking')
    context = {'partners': partners, 'link_partners': link_partners}
    return render(request, 'partner/partners.html', context)

def PartnerView(request,partner_name):
    """ renders partner and corresponding experts and courses in its own partner page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    experts = Expert.objects.filter(is_active=True).filter(partner=partner)
    partner_courses = PartnerCourse.objects.filter(is_active=True).filter(partner=partner)
    courses = []
    for partner_course in partner_courses:
        course_key = CourseKey.from_string(partner_course.course_id)
        courseoverview = CourseOverview.get_from_id(course_key)
        courses.append(courseoverview)
    is_multiple_courses = len(courses) > 1
    context = {'partner': partner,  'courses': courses,
               'experts': experts, 'is_multiple_courses': is_multiple_courses}
    return render(request, 'partner/partner.html', context)

def PartnerCourseView(request,partner_name,course_id):
    """ renders course in its own course page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    partner_course = get_object_or_404(PartnerCourse, course_id=course_id)
    course_key = CourseKey.from_string(course_id)
    course = CourseOverview.get_from_id(course_key)
    context = {'partner': partner, 'ppartner/artner_course': partner_course, 'course': course}
    return render(request, 'partner_course.html', context)

def ExpertView(request,partner_name,expert_id):
    """ renders expert in its own expert page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    expert = get_object_or_404(Expert, pk=expert_id)
    partner_courses = PartnerCourse.objects.filter(experts__id__exact=expert_id)
    courses = []
    for partner_course in partner_courses:
        course_key = CourseKey.from_string(partner_course.course_id)
        courseoverview = CourseOverview.get_from_id(course_key)
        courses.append({'courseoverview':courseoverview, 'partner_course':partner_course})
    context = {'partner': partner, 'expert': expert, 'courses': courses}
    return render(request, 'partner/expert.html', context)

# get list of all existing course ids
# list_of_all_course_ids = CourseOverview.get_all_course_keys()

