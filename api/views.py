from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *

# Create your views here.

#######################################################
#
# Faculty
#
#######################################################
@csrf_exempt
def faculty_list(request):
    
    if request.method == 'GET':
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FacultySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def faculty_details(request, pk):
    
    try:
        faculty = Faculty.objects.get(uuid=pk)
    except Faculty.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FacultySerializer(faculty, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        faculty.delete()
        return HttpResponse(status=204)

#######################################################
#
# Department
#
#######################################################
@csrf_exempt
def department_list(request):
    
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def department_details(request, pk):
    
    try:
        department = Department.objects.get(uuid=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        return HttpResponse(status=204)

#######################################################
#
# Session
#
#
#######################################################
@csrf_exempt
def session_list(request):
    
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SessionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def session_details(request, pk):
    
    try:
        session = Session.objects.get(uuid=pk)
    except Session.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SessionSerializer(session)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SessionSerializer(session, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        session.delete()
        return HttpResponse(status=204)


#######################################################
#
# Sesmester
#
#######################################################
@csrf_exempt
def semester_list(request):
    
    if request.method == 'GET':
        semesters = Semester.objects.all()
        serializer = SemesterSerializer(semesters, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SemesterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def semester_details(request, pk):
    
    try:
        semester = Semester.objects.get(uuid=pk)
    except Semester.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SemesterSerializer(semester)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SemesterSerializer(semester, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        semester.delete()
        return HttpResponse(status=204)

#######################################################
#
# Programme
#
#######################################################
@csrf_exempt
def programme_list(request):
    
    if request.method == 'GET':
        programme = Programme.objects.all()
        serializer = ProgrammeSerializer(programme, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProgrammeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def programme_details(request, pk):
    
    try:
        programme = Programme.objects.get(uuid=pk)
    except Semester.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProgrammeSerializer(programme)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProgrammeSerializer(programme, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        programme.delete()
        return HttpResponse(status=204)

@csrf_exempt
def user_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


#######################################################
#
# Students
#
#######################################################
@csrf_exempt
def student_list(request):
    
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentDetailsSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        # create a user first
        user = User(first_name=data["first_name"],middle_name=data["middle_name"], last_name=data["last_name"], user_type=UserType.STUDENT,)
        user.save()

        # update student uuid with 
        data["uuid"] = user.uuid

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_details(request, pk):
    
    try:
        student = Student.objects.get(uuid=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentDetailsSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)

#######################################################
#
# Staff
#
#######################################################
@csrf_exempt
def staff_list(request):
    
    if request.method == 'GET':
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        # create a user first
        user = User(first_name=data["first_name"], middle_name=data["middle_name"], last_name=data["last_name"], user_type=UserType.STAFF,)
        user.save()

        # update student uuid with 
        data["uuid"] = user.uuid

        serializer = StaffSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def staff_details(request, pk):
    
    try:
        staff = Staff.objects.get(uuid=pk)
    except Staff.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StaffSerializer(staff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        staff.delete()
        return HttpResponse(status=204)

#######################################################
#
# Staff Roles
#
#######################################################
@csrf_exempt
def roles_list(request):
    
    if request.method == 'GET':
        staff = StaffRole.objects.all()
        serializer = StaffRoleSerializer(staff, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = StaffRoleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def roles_details(request, pk):
    
    try:
        role = StaffRole.objects.get(uuid=pk)
    except StaffRole.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StaffRoleSerializer(role)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StaffRoleSerializer(role, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        role.delete()
        return HttpResponse(status=204)

#######################################################
#
# Course
#
#######################################################
@csrf_exempt
def course_list(request):
    
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

@csrf_exempt
def course_details(request, pk):
    
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

@csrf_exempt
def course_enrollment(request, pk, semester, programme):

    try:
        course = Course.objects.get(uuid=pk)
        semester = Semester.objects.get(uuid=semester)
        programme = Programme.objects.get(uuid=programme)
        course_cycle = CourseCycle.objects.get_or_create(semster=semester, course=course, programme=programme)
    except Programme.DoesNotExist:
        return HttpResponse('No Such Programme Exist', status=404)
    except Semester.DoesNotExist:
        return HttpResponse('No Such Semester Exist', status=404)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    except CourseCycle.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        students = StudentEnrollment.objects.all().filter(course_cycle=course_cycle[0].uuid)
        student_uuids = [Student.objects.get(uuid=i['student_id']) for i in students.values()]

        stdents = StudentSerializer(student_uuids, many=True).data
        serializer = CourseCycleSerializer(course_cycle[0], context={'students': stdents, 'staff': [], 'schedules':[]})
        
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = StudentEnrollmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = StudentEnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = StudentEnrollmentSerializer(data=data)
        if serializer.is_valid():
            enrollment = StudentEnrollment.objects.get(course_cycle=course_cycle[0].uuid, student=data['student'])
            enrollment.delete()
            return HttpResponse('A student has been removed',status=204)
        return JsonResponse(serializer.errors, status=400)
        

@csrf_exempt
def course_assignment(request, pk, semester, programme):

    try:
        course = Course.objects.get(uuid=pk)
        semester = Semester.objects.get(uuid=semester)
        programme = Programme.objects.get(uuid=programme)
        course_cycle = CourseCycle.objects.get_or_create(semster=semester, course=course, programme=programme)
    except Programme.DoesNotExist:
        return HttpResponse('No Such Programme Exist', status=404)
    except Semester.DoesNotExist:
        return HttpResponse('No Such Semester Exist', status=404)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    except CourseCycle.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        staff = TeacherAssigned.objects.all().filter(course_cycle=course_cycle[0].uuid)
        staff_uuids = [Student.objects.get(uuid=i['staff_id']) for i in staff.values()]
        staff = StaffSerializer(staff_uuids, many=True).data
        serializer = CourseCycleSerializer(course_cycle[0], context={'staff': staff, 'students':[], 'schedules':[]})
        
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TeacherAssignedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TeacherAssignedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TeacherAssignedSerializer(data=data)
        if serializer.is_valid():
            enrollment = TeacherAssigned.objects.get(course_cycle=course_cycle[0].uuid, staff=data['staff'])
            enrollment.delete()
            return HttpResponse('A teacher has been removed',status=204)
        return JsonResponse(serializer.errors, status=400)

#######################################################
#
# Course Schedule
#
#######################################################
@csrf_exempt
def course_schedule(request, pk, semester, programme):

    try:
        course = Course.objects.get(uuid=pk)
        semester = Semester.objects.get(uuid=semester)
        programme = Programme.objects.get(uuid=programme)
        course_cycle = CourseCycle.objects.get_or_create(semster=semester, course=course, programme=programme)
    except Programme.DoesNotExist:
        return HttpResponse('No Such Programme Exist', status=404)
    except Semester.DoesNotExist:
        return HttpResponse('No Such Semester Exist', status=404)
    except Course.DoesNotExist:
        return HttpResponse('No Such Course Exist', status=404)
    except CourseCycle.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        schedule = TimeScheduleAssigned.objects.all().filter(course_cycle=course_cycle[0].uuid)        
        schedule = TimeScheduleAssignedSerializer(schedule, many=True).data
        serializer = CourseCycleSerializer(course_cycle[0], context={'schedule':schedule, 'staff': [], 'students':[]})
        
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TimeScheduleAssignedSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TimeScheduleAssignedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        data['course_cycle'] = course_cycle[0].uuid

        serializer = TimeScheduleAssignedSerializer(data=data)
        if serializer.is_valid():
            schedule = TimeScheduleAssigned.objects.get(course_cycle=course_cycle[0].uuid, schedule=data['schedule'])
            schedule.delete()
            return HttpResponse('A class schedule has been removed',status=204)
        return JsonResponse(serializer.errors, status=400)

def index(request):
    return HttpResponse("API is Live")