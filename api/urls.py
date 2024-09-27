from django.urls import path

from api.endpoints import course_cycles, courses

from . import views

urlpatterns = [
    path('calender/', views.calender_list, name='current_calender'),
    path('calender/add', views.calender_list, name='add_calender'),
    path('calender/edit/<uuid:pk>', views.calender_details, name='edit_calender'),

    path('courses/', courses.list, name='course_list'),
    path('courses/<uuid:pk>', courses.details, name='course_details'),
    path('courses/<uuid:pk>/cycles', views.course_cycles, name='course_cycles'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/enroll', views.course_enrollment, name='course_enrollment'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/teachers', views.course_assignment, name='course_assignment'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/schedule', views.course_schedule, name='course_schedule'),
    
    path('courses/<uuid:pk>/staff', courses.staff_list, name='assigned_staff'),
    path('courses/staff/remove/<uuid:pk>', courses.remove_staff, name='remove_staff'),
    path('courses/<uuid:pk>/students', courses.student_list, name='enrolled_students'),
    # path('courses/<uuid:pk>/timetable', views.course_details, name='course_details'),
    # path('courses/<uuid:pk>/materials', views.course_details, name='course_details'),
    # path('courses/<uuid:pk>/assignments', views.course_details, name='course_details'),

    path('cycles/', course_cycles.list, name='cycles_list'),
    path('cycles/query', course_cycles.get_cycle, name='cycles_detail'),

    path('cycles/current/<uuid:course>', course_cycles.current, name='cycles_current'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/<uuid:pk>', views.department_details, name='department_details'),

    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/<uuid:pk>', views.faculty_details, name='faculty_details'),
    path('faculty/<uuid:pk>/departments', views.faculty_with_departments, name='faculty_with-departments'),

    path('programme/', views.programme_list, name='programme_list'),
    path('programme/<uuid:pk>', views.programme_details, name='programme_details'),

    path('roles/', views.roles_list, name='roles_list'),
    path('roles/<uuid:pk>', views.roles_details, name='roles_details'),
    # path('roles/<uuid:staff>', views.roles_assign, name='roles_assign'),

    path('students/', views.student_list, name='student_list'),
    path('students/<uuid:pk>', views.student_details, name='student_details'),
    path('students/<uuid:pk>/<uuid:programme>/<uuid:semester>/', views.student_courses, name='student_courses'),

    path('profile/', views.profile_list, name='profile_list'),
    path('profile/<uuid:pk>', views.profile_details, name='profile_details'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<uuid:pk>', views.staff_details, name='staff_details'),

    path('sessions/', views.session_list, name='session_list'),
    path('sessions/programme/<uuid:programme>', views.session_filter, name='session_filter'),
    path('sessions/<uuid:pk>', views.session_details, name='session_details'),

    path('semesters/', views.semester_list, name='semester_list'),
    path('semesters/session/<uuid:session>', views.semester_filter, name='semester_filter'),
    path('semesters/<uuid:pk>', views.semester_details, name='semester_details'),

    path('login/', views.login, name='user_login'),

    path("", views.index, name="index"),
]