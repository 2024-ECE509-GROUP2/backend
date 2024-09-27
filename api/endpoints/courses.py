from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Course, CourseCycle, StudentEnrollment, TeacherAssigned
from api.serializers import CourseSerializer, StudentEnrollmentDetailsSerializer, StudentEnrollmentSerializer, TeacherAssignedDetailsSerializer, TeacherAssignedSerializer


#######################################################
#
# Courses
# 
# ../api/v1/courses/
#
#######################################################


# ../api/v1/courses/
@csrf_exempt
def list(request):
    
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = CourseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# 
# ../api/v1/courses/<uuid>  (uuid -- the unique id of the course)
@csrf_exempt
def details(request, pk):
    
    try:
        course = Course.objects.get(uuid=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=204)

# ../api/v1/courses/<uuid>/staff  (uuid -- the unique id of the course)
@csrf_exempt
def staff_list(request, pk):
    
    if request.method == 'GET':
        
        cycles = CourseCycle.objects.all().filter(course=pk)
        teacher_list = TeacherAssigned.objects.all().filter(course_cycle__in=cycles)

        cycle = request.GET.get('cycle')
        if(cycle):
            teacher_list = TeacherAssigned.objects.all().filter(course_cycle=cycle)

        serializer = TeacherAssignedDetailsSerializer(teacher_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = TeacherAssignedSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
# ../api/v1/courses/<uuid>/students  (uuid -- the unique id of the course)
@csrf_exempt
def student_list(request, pk):
    
    if request.method == 'GET':
        
        cycles = CourseCycle.objects.all().filter(course=pk)
        student_list = StudentEnrollment.objects.all().filter(course_cycle__in=cycles)

        cycle = request.GET.get('cycle')
        if(cycle):
            student_list = StudentEnrollment.objects.all().filter(course_cycle=cycle)

        serializer = StudentEnrollmentDetailsSerializer(student_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = StudentEnrollmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# ../api/v1/courses/staff/remove/<uuid>  (uuid -- the unique id of the staffassignment i.e TeacherAssigned)
@csrf_exempt
def remove_staff(request, pk):

    try:
        assignment = TeacherAssigned.objects.get(uuid=pk)
    except TeacherAssigned.DoesNotExist:
        return JsonResponse({'message': 'does not exist'}, status=404)
    
    if request.method == 'DELETE':
        assignment.delete()
        return JsonResponse({'message': 'removed staff assignment'}, safe=False, status=204)

# ../api/v1/courses/staff/edit/<uuid>  (uuid -- the unique id of the staffassignment i.e TeacherAssigned)
@csrf_exempt
def edit_staff(request, pk):

    try:
        assignment = TeacherAssigned.objects.get(course=pk)
    except TeacherAssigned.DoesNotExist:
        return JsonResponse({'message': 'does not exist'}, status=404)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherAssignedSerializer(assignment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



# ../api/v1/courses/<uuid>/staff  (uuid -- the unique id of the course)
@csrf_exempt
def staff_details(request, pk):
    
    try:
        teacher_list = TeacherAssigned.objects.get(course=pk)
    except TeacherAssigned.DoesNotExist:
        return JsonResponse({'message': 'does not exist'}, status=404)

    if request.method == 'GET':

        serializer = TeacherAssignedSerializer(teacher_list)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherAssignedSerializer(teacher_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        teacher_list.delete()
        return HttpResponse(status=204)