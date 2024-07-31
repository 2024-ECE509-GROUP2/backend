
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid
# Create your models here.

class Session(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_label = models.CharField(max_length=60)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Faculty(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty_name = models.CharField(max_length=256)
    session_created = models.ForeignKey(Session, on_delete=models.PROTECT, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Department(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    department_name = models.CharField(max_length=256)
    department_code = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Semester(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    semester_label = models.CharField(max_length=60)
    semester_count = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Programme(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    programme_label = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class UserType(models.TextChoices):
    STUDENT = "student", _("Student")
    STAFF = "staff", _("Staff")

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(choices=UserType, max_length=8)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()

class Student(models.Model):
    uuid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    department_joined = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, related_name='+')
    session_joined = models.ForeignKey(Session, on_delete=models.PROTECT, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class StaffRole(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_label = models.CharField(max_length=60)
    role_description = models.CharField(max_length=256)
    role_code = models.CharField(max_length=10, null=True)
    roles = models.BinaryField()

class Staff(models.Model):
    uuid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10, null=True)
    role = models.ForeignKey(StaffRole, on_delete=models.SET_NULL, null=True, blank=True)

class Course(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=256)
    course_code = models.CharField(max_length=256)
    course_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class CourseCycle(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semster = models.ForeignKey(Semester, on_delete=models.PROTECT)
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class TeacherAssigned(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    is_supervisor = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class StudentEnrollment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class StudentGradesEarned(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    points_earned = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class AssignmentsAssigned(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    assignment_description = models.TextField()
    max_points_earnable = models.FloatField()
    date_deadline = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class AssignmentsSubmissions(models.Model):
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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_cycle = models.ForeignKey(CourseCycle, on_delete=models.PROTECT)
    weekday = models.IntegerField(choices=WeekDay, null=True)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



