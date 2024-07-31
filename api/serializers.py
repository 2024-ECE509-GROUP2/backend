from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['uuid', 'user_type', 'first_name', 'last_name', 'middle_name', 'email',]

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['uuid', 'student_id', 'department', 'department_joined', 'session_joined']

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['uuid', 'student_id', 'department', 'department_joined', 'session_joined']

class StudentDetailsSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='uuid.first_name')
    last_name = serializers.CharField(source='uuid.last_name')
    middle_name = serializers.CharField(source='uuid.middle_name')
    email = serializers.CharField(source='uuid.email')

    class Meta:
        model = Student
        read_only_fields = ['uuid']
        fields = ['uuid', 'student_id', 'department', 
        'department_joined', 'session_joined', 'first_name',
        'last_name', 'middle_name', 'email']

class StaffRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffRole
        fields = ['uuid', 'role_label', 'role_description', 'role_code']

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['uuid', 'staff_id', 'role',]

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ['uuid', 'faculty_name', 'session_created']

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['uuid', 'department_name', 'faculty']

class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ['uuid', 'session_label', 'date_start', 'date_end']

class SemesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ['uuid', 'session', 'semester_label', 'semester_count', 'date_start', 'date_end']

class ProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        fields = ['uuid', 'programme_label']

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['uuid', 'course_name', 'course_code', 'course_description']

class CourseCycleSerializer(serializers.ModelSerializer):

    students = serializers.JSONField(read_only=True)
    staff = serializers.JSONField(read_only=True)
    schedules = serializers.JSONField(read_only=True)

    class Meta:
        model = CourseCycle
        fields = ['uuid', 'course', 'semster', 'programme', 'staff', 'students', 'schedules']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if(self.context['students']):
            representation['students'] = self.context['students']

        if(self.context['staff']):
            representation['staff'] = self.context['staff']

        if(self.context['schedules']):
            representation['schedules'] = self.context['schedules']

        return representation

class TeacherAssignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherAssigned
        fields = ['uuid', 'course_cycle', 'staff', 'is_supervisor']

class StudentEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentEnrollment
        fields = ['uuid', 'course_cycle', 'student']

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
