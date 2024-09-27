from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import CourseCycle, SchoolCalender
from api.serializers import CourseCycleDefaultSerializer, CourseCycleDetailSerializer


#######################################################
#
# Courses Cycles
# 
# ../api/v1/cycles/
#
#######################################################


# ../api/v1/cycles
# parameters
#   course: filters the query with course
@csrf_exempt
def list(request):
    
    if request.method == 'GET':

        #Get All Cycles
        course_cycle = CourseCycle.objects.all()
        
        programme = request.GET.get('programme', '')
        if programme:
            # filter by course
            course_cycle = course_cycle.filter(programme=programme)

        semester = request.GET.get('semester', '')
        if semester:
            # filter by course
            course_cycle = course_cycle.filter(semster=semester) # the semster is a typo (fix later)

        course = request.GET.get('course', '')
        if course:
            # filter by course
            course_cycle = course_cycle.filter(course=course)
                
        serializer = CourseCycleDetailSerializer(course_cycle, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = CourseCycleDefaultSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

# ../api/v1/cycles (uuid - primary key for course)
# Get Cycle
@csrf_exempt
def get_cycle(request):
    
    if request.method == 'GET':

        programme = request.GET.get('programme', '')

        if not programme:
            # If no Programme is specfied, it is a bad request
            return JsonResponse({'message': 'Specify Programme'}, status=400) 
        
        course = request.GET.get('course', '')

        if not course:
            # If no Course is specfied, it is a bad request
            return JsonResponse({'message': 'Specify Course'}, status=400) 
        
        semester = request.GET.get('semester', '')

        if not semester:
            # If no semester is specfied, it is a bad request
            return JsonResponse({'message': 'Specify Semester'}, status=400) 

        course_cycle = CourseCycle.objects.get_or_create(semster=semester, course=course, programme=programme)
        serializer = CourseCycleDefaultSerializer(course_cycle[0])
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

# ../api/v1/cycles/<uuid> (uuid - primary key for course)
# Get Current Cycle
@csrf_exempt
def current(request, course):
    
    if request.method == 'GET':

        programme = request.GET.get('programme', '')

        if not programme:
            # If no Programme is specfied, it is a bad request
            return JsonResponse({'message': 'Specify Programme'}, status=400) 
        
        # Get from calender for programme
        calender = SchoolCalender.objects.get(programme=programme)

        # If there is no ongoing session, it is not a a bad request but we need to handle the error 
        if(calender.current_session == None):
            return JsonResponse({'message': 'No Ongoing Session'}, status=200) # 
        
        # same thing for semesters, it is not a a bad request but we need to handle the error 
        if(calender.current_semester == None):
            return JsonResponse({'message': 'No Ongoing Semester'}, status=200)

        course_cycle = CourseCycle.objects.get_or_create(semster=calender.current_semester, course=course, programme=programme)
        serializer = CourseCycleDefaultSerializer(course_cycle[0])
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)
    
    