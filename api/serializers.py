from types import NoneType
from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = ['uuid']
        fields = ['uuid', 'user_type', 'profile_url', 'first_name', 'last_name', 'middle_name', 'email',]

class CalenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolCalender
        read_only_fields = ['uuid']
        fields = ['uuid', 'programme', 'current_semester',]

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['uuid', 'student_id', 'department', 'department_joined', 'session_joined']

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        read_only_fields = ['uuid']
        fields = ['uuid', 'student_id', 'department', 'department_joined', 'session_joined']

class StudentDetailsSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='uuid.first_name')
    last_name = serializers.CharField(source='uuid.last_name')
    middle_name = serializers.CharField(source='uuid.middle_name')
    email = serializers.CharField(source='uuid.email')
    profile_url = serializers.CharField(source='uuid.profile_url')

    department_name = serializers.CharField(source='department.department_name')
    department_joined_name = serializers.CharField(source='department_joined.department_name')
    session_label = serializers.CharField(source='session_joined.session_label')

    class Meta:
        model = Student
        read_only_fields = ['uuid']
        fields = ['uuid', 'student_id', 'department', 'department_name', 
        'department_joined', 'department_joined_name', 'session_label','session_joined', 'first_name',
        'last_name', 'middle_name', 'email', 'profile_url']

class StaffRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffRole
        read_only_fields = ['uuid']
        fields = ['uuid', 'role_label', 'role_description', 'role_code']

class StaffRoleUUIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffRole
        fields = ['uuid']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['uuid']    

class StaffRoleNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffRole
        fields = ['role_label']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['role_label']

class StaffSerializer(serializers.ModelSerializer):


    class Meta:
        model = Staff
        read_only_fields = ['roles']
        fields = ['uuid', 'staff_id', 'roles']

class StaffDetailsSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='uuid.first_name')
    last_name = serializers.CharField(source='uuid.last_name')
    middle_name = serializers.CharField(source='uuid.middle_name')
    email = serializers.CharField(source='uuid.email')
    profile_url = serializers.CharField(source='uuid.profile_url')

    # department_name = serializers.CharField(source='department.department_name')

    roles = serializers.ListField(child= StaffRoleUUIDSerializer(),source='roles.all', )
    roles_labels = serializers.ListField(child= StaffRoleNameSerializer(),source='roles.all', )
    
    class Meta:
        model = Staff
        read_only_fields = ['uuid']
        fields = ['uuid',  'first_name', 'staff_id',  'roles_labels', 'roles',
        'last_name', 'middle_name', 'email', 'profile_url']

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        read_only_fields = ['uuid']
        fields = ['uuid', 'faculty_name', 'session_created']

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        read_only_fields = ['uuid']
        fields = ['uuid', 'department_name', 'department_code', 'faculty']
    
class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        read_only_fields = ['uuid']
        fields = ['uuid', 'session_label', 'programme', 'has_started', 'date_start', 'has_ended', 'date_end']

class SemesterSerializer(serializers.ModelSerializer):

    semester_label = serializers.SerializerMethodField()

    class Meta:
        model = Semester
        read_only_fields = ['uuid']
        fields = ['uuid', 'session', 'semester_label', 'semester_count', 'date_start', 'date_end']

    def get_semester_label(self, obj):
        
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

        return f'{obj.session.session_label} {ordinal(obj.semester_count)} Semester'

class ProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        read_only_fields = ['uuid']
        fields = ['uuid', 'programme_label']

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        read_only_fields = ['uuid']
        fields = ['uuid', 'course_name', 'course_code', 'allowed_departments', 'course_description']

class CourseCycleDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCycle
        read_only_fields = ['uuid']
        fields = ['uuid', 'course', 'semster', 'programme']
    
class CourseCycleDetailSerializer(serializers.ModelSerializer):

    course = CourseSerializer()
    semster = SemesterSerializer()
    programme = ProgrammeSerializer()

    class Meta:
        model = CourseCycle
        read_only_fields = ['uuid']
        fields = ['uuid', 'course', 'semster', 'programme']

class TeacherAssignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherAssigned
        fields = ['uuid', 'course_cycle', 'staff', 'is_supervisor']

class TeacherAssignedDetailsSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='staff.uuid.first_name')
    last_name = serializers.CharField(source='staff.uuid.last_name')
    middle_name = serializers.CharField(source='staff.uuid.middle_name')
    email = serializers.CharField(source='staff.uuid.email')

    roles = serializers.ListField(child= StaffRoleUUIDSerializer(),source='staff.roles.all', )
    role_labels = serializers.ListField(child= StaffRoleNameSerializer(),source='staff.roles.all', )

    class Meta:
        model = TeacherAssigned
        read_only_fields = ['uuid']
        fields = ['uuid', 'course_cycle', 'staff', 'is_supervisor', 'first_name',  
        'last_name', 'middle_name', 'email', 'roles', 'role_labels',]

class StudentEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentEnrollment
        fields = ['uuid', 'course_cycle', 'student', 'approved']

class StudentEnrollmentDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentEnrollment
        fields = ['uuid', 'course_cycle', 'student', 'approved']
    
    def to_representation(self, instance):

        representation = super().to_representation(instance)

        student = Student.objects.get(uuid=representation['student'])
        student = StudentDetailsSerializer(student)

        representation['student'] = student.data

        return representation

class StudentGradesEarnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGradesEarned
        fields = ['uuid', 'course_cycle', 'student', 'points_earned']

class AssignmentsAssignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssignmentsAssigned
        fields = ['uuid', 'course_cycle', 'assignment_description', 'max_points_earnable']

class AssignmentsSubmissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssignmentsSubmissions
        fields = ['uuid', 'course_cycle', 'assignment', 'submission_description', 'submission_date', 'has_been_marked', 'points_earned']

class TimeScheduleAssignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeScheduleAssigned
        fields = ['uuid', 'course_cycle', 'time_start', 'time_end']


# This custom serializer also gets the departments of the faculty
class FacultyWithDepartmentSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Faculty
        read_only_fields = ['uuid']
        fields = ['uuid', 'faculty_name', 'session_created']

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        departments = Department.objects.all().filter(faculty=representation['uuid'])
        departments = DepartmentSerializer(departments, many=True)

        representation['departments'] = departments.data

        return representation
    

class ProgrammeBigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        read_only_fields = ['uuid']
        fields = ['uuid', 'programme_label']
    
    def to_representation(self, instance):

        representation = super().to_representation(instance)

        sessions = Session.objects.all().filter(programme=representation['uuid'])
        sessions = SessionSerializer(sessions, many=True)

        representation['sessions'] = sessions.data

        return representation
    
class SessionBigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        read_only_fields = ['uuid']
        fields = ['uuid', 'session_label', 'programme', 'has_started', 'date_start', 'has_ended', 'date_end']

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        semesters = Semester.objects.all().filter(session=representation['uuid'])
        semesters = SemesterSerializer(semesters, many=True)

        representation['semesters'] = semesters.data

        return representation

class CalenderBigSerializer(serializers.ModelSerializer):

    programme_label = serializers.CharField(source="programme.programme_label")

    class Meta:
        model = SchoolCalender
        read_only_fields = ['uuid']
        fields = ['uuid', 'programme', 'programme_label', 'current_semester']

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        try:
            semester_details = Semester.objects.get(uuid=representation['current_semester'])
            session_details = Semester.objects.get(uuid=representation['current_semester']).session

            semester_details = SemesterSerializer(semester_details)
            representation['semester_details'] = semester_details.data

            session_details = SessionSerializer(session_details)
            representation['session_details'] = session_details.data
        except Semester.DoesNotExist:
            representation['semester_details'] = None
        except Session.DoesNotExist:
            representation['session_details'] = None

        return representation