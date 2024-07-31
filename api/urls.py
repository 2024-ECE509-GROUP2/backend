from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<uuid:pk>', views.course_details, name='course_details'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/enroll', views.course_enrollment, name='course_enrollment'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/teachers', views.course_assignment, name='course_assignment'),
    path('courses/<uuid:pk>/<uuid:programme>/<uuid:semester>/schedule', views.course_schedule, name='course_schedule'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<uuid:pk>', views.department_details, name='department_details'),
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/<uuid:pk>', views.faculty_details, name='faculty_details'),
    path('programme/', views.programme_list, name='programme_list'),
    path('programme/<uuid:pk>', views.programme_details, name='programme_details'),
    path('roles/', views.roles_list, name='roles_list'),
    path('roles/<uuid:pk>', views.roles_details, name='roles_details'),
    path('students/', views.student_list, name='student_list'),
    path('students/<uuid:pk>', views.student_details, name='student_details'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<uuid:pk>', views.staff_details, name='staff_details'),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/<uuid:pk>', views.session_details, name='session_details'),
    path('semesters/', views.semester_list, name='semester_list'),
    path('semesters/<uuid:pk>', views.semester_details, name='semester_details'),
    path('users/', views.user_list, name='user_list'),
    path("", views.index, name="index"),
]