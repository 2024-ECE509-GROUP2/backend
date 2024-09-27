
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

from requests import session
# Create your models here.

#moved Programme to the top for Session to access it

class Programme(models.Model):
    
    def __str__(self):
        return self.programme_label
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    programme_label = models.CharField(max_length=256)
    session_count = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Session(models.Model):
    
    def __str__(self):
        return self.session_label
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT,)
    session_label = models.CharField(max_length=60)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, default=None)
    has_started = models.BooleanField(default=False,)
    has_ended = models.BooleanField(default=False,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Semester(models.Model):

    def __str__(self):

        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        return f'{self.session.session_label} {ordinal(self.semester_count)} Semester'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    semester_count = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)    

#now each can point the ongoing session.
#now each can point to the latest semester
class SchoolCalender(models.Model):

    def __str__(self):

        return f' {self.programme.programme_label}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    programme = models.OneToOneField(Programme, on_delete=models.PROTECT, )
    current_semester = models.ForeignKey(Semester, on_delete=models.PROTECT, null=True)

class Faculty(models.Model):

    def __str__(self):
        return self.faculty_name
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty_name = models.CharField(max_length=256)
    session_created = models.ForeignKey(Session, on_delete=models.PROTECT, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Department(models.Model):

    def __str__(self):

        return self.department_name
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    department_name = models.CharField(max_length=256)
    department_code = models.CharField(max_length=10, null=True)
    past_student_count = models.IntegerField(default=0,)
    past_staff_count = models.IntegerField(default=0,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class UserType(models.TextChoices):
    STUDENT = "student", _("Student")
    STAFF = "staff", _("Staff")

class User(models.Model):

    def __str__(self):

        return f'{self.first_name} {self.last_name} Profile'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(choices=UserType, max_length=8)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    profile_url= models.TextField(null=True)
    email = models.EmailField()

class Student(models.Model):
    def __str__(self):

        return f'{self.uuid.first_name} {self.uuid.last_name}'
    
    uuid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15, unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    department_joined = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, related_name='+')
    session_joined = models.ForeignKey(Session, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

# removed the is_active field, is not used
class StaffRole(models.Model):
    def __str__(self):

        return f'{self.role_label}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_label = models.CharField(max_length=60)
    role_description = models.CharField(max_length=256)

class Staff(models.Model):

    def __str__(self):

        return f'{self.uuid.first_name} {self.uuid.last_name}'
    
    uuid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=15, unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True,)
    date_joined = models.DateTimeField(auto_now_add=True)
    roles = models.ManyToManyField(StaffRole)

# the allowed departments is so we can see which students have access to the course
class Course(models.Model):

    def __str__(self):

        return f'{self.course_name}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=256)
    course_code = models.CharField(max_length=256)
    course_description = models.TextField()
    allowed_departments = models.ManyToManyField(Department)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class CourseCycle(models.Model):

    def __str__(self):

        return f' {self.course.course_name} During {self.semster.__str__()} {self.programme.programme_label} '
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semster = models.ForeignKey(Semester, on_delete=models.PROTECT)
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class TeacherAssigned(models.Model):

    def __str__(self):

        return f' {self.staff.__str__()} Assignment For {self.course_cycle.__str__()}'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    is_supervisor = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class StudentEnrollment(models.Model):

    def __str__(self):

        return f' {self.student.__str__()} Enrollment For {self.course_cycle.__str__()}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class StudentGradesEarned(models.Model):

    def __str__(self):

        return f' {self.student.__str__()} Grade For {self.course_cycle.__str__()}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    points_earned = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class AssignmentsAssigned(models.Model):

    def __str__(self):

        return f'Cycle: {self.course_cycle.__str__()}, {self.assignment_description}'
    

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    assignment_description = models.TextField()
    max_points_earnable = models.FloatField()
    date_deadline = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class AssignmentsSubmissions(models.Model):

    def __str__(self):

        return f'Cycle: {self.course_cycle.__str__()}, {self.assignment.assignment_description}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    assignment = models.ForeignKey(AssignmentsAssigned, on_delete=models.PROTECT)
    submission_description = models.TextField()
    submission_date = models.DateTimeField()
    has_been_marked = models.BooleanField(default=False)
    points_earned = models.ForeignKey(StudentGradesEarned, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class WeekDay(models.IntegerChoices):
    MONDAY = 1, _("Monday")
    TUESDAY = 2, _("Tuesday")
    WEDNESDAY = 3, _("Wednesday")
    THURSDAY = 4, _("Thursday")
    FRIDAY = 5, _("Friday")
    SATURDAY = 6, _("Saturday")
    SUNDAY = 7, _("Sunday")

class TimeScheduleAssigned(models.Model):
    def __str__(self):

        return f'Cycle: {self.course_cycle.__str__()}'
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    weekday = models.IntegerField(choices=WeekDay, null=True)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
