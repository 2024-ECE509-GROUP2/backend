from django.contrib import admin
from api.models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(StaffRole)
admin.site.register(User)

admin.site.register(Course)
admin.site.register(CourseCycle)

admin.site.register(Faculty)
admin.site.register(Department)

admin.site.register(SchoolCalender)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Programme)

admin.site.register(AssignmentsAssigned)
admin.site.register(AssignmentsSubmissions)

admin.site.register(TeacherAssigned)

admin.site.register(TimeScheduleAssigned)

admin.site.register(StudentEnrollment)
admin.site.register(StudentGradesEarned)

