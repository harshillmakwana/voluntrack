from django.contrib import admin
from django.urls import path,include
from . import views

# app_name = 'adminapp'
urlpatterns = [
    path('myname/',views.myname,name='myname'),
    
    # template urls   
    path('apply_event_view/',views.apply_event_view,name='apply_event_view'),# {% url "apply_event_view" %}
    path('attendance_history_view/',views.attendance_history_view,name='attendance_history_view'),# {% url "attendance_history_view" %}
    path('certificates_view/',views.certificates_view,name='certificates_view'),# {% url "certificates_view" %}
    path('checkin_view/',views.checkin_view,name='checkin_view'),# {% url "checkin_view" %}
    path('checkout_view/',views.checkout_view,name='checkout_view'),# {% url "checkout_view" %}
    path('dashboard_view_ad/',views.dashboard_view_ad,name='dashboard_view_ad'),# {% url "dashboard_view" %}
    path('event_detail_view/',views.event_detail_view,name='event_detail_view'),# {% url "event_detail_view" %}
    path('event_list_view/',views.event_list_view,name='event_list_view'),# {% url "event_list_view" %}
    path('forgot_password_view/',views.forgot_password_view,name='forgot_password_view'),#{% url "forgot_password_view" %}
    path('login_view/',views.login_view,name='login_view'),# {% url "login_view" %}
    path('my_applications_view/',views.my_applications_view,name='my_applications_view'),# {% url "my_applications_view" %}
    path('my_tasks_view/',views.my_tasks_view,name='my_tasks_view'),# {% url "my_tasks_view" %}
    path('profile_edit_view/',views.profile_edit_view,name='profile_edit_view'),#{% url "profile_edit_view" %}
    path('profile_view_view/',views.profile_view_view,name='profile_view_view'),# {% url "profile_view_view" %}
    path('register_view/',views.register_view,name='register_view'),# {% url "register_view" %}
    path('reset_password_view/',views.reset_password_view,name='reset_password_view'),#{% url "reset_password_view" %}
    path('all_users/',views.all_users,name='all_users_view'),# {% url "all_users" %}
    path('update_status/<int:user_id>/<str:action>/', views.update_status, name='update_status'),# {% url "update_status" user.id 'approve' %}
    path('admin_profile/',views.admin_profile,name='admin_profile'),# {% url "admin_profile" %}
    
    
       
    #model and list urls
    path('create_Event/',views.create_Event,name='create_Event'),
    path('list_Event/',views.list_Event,name='list_Event'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),
    path('update_event/<int:id>',views.update_event,name='update_event'),
    
    
    path('create_EventRole/',views.create_EventRole,name='create_EventRole'),
    path('list_EventRole/',views.list_EventRole,name='list_EventRole'),
    path('detete_role/<int:id>/',views.detete_role,name='detete_role'),
    path('update_EventRole/<int:id>/',views.update_EventRole,name='update_EventRole'),
    
    
    
    path('create_VolunteerApplication/',views.create_VolunteerApplication,name='create_VolunteerApplication'),
    path('list_VolunteerApplication/',views.list_VolunteerApplication,name='list_VolunteerApplication'),
    path('delete_volappli/<int:id>/',views.delete_volappli,name='delete_volappli'),
    path('update_VolunteerApplication/<int:id>/',views.update_VolunteerApplication,name='update_VolunteerApplication'),
    
    
    path('create_TaskAssignment/',views.create_TaskAssignment,name='create_TaskAssignment'),
    path('list_TaskAssignment/',views.list_TaskAssignment,name='list_TaskAssignment'),
    path('delete_taskassi/<int:id>/',views.delete_taskassi,name='delete_taskassi'),
    path('update_TaskAssignment/<int:id>/',views.update_TaskAssignment,name='update_TaskAssignment'),
    
    
    path('create_Attendance/',views.create_Attendance,name='create_Attendance'),
    path('list_Attendance/',views.list_Attendance,name='list_Attendance'),
    path('delete_attedance/<int:id>/',views.delete_attedance,name='delete_attedance'),
    path('update_Attendance/<int:id>/',views.update_Attendance,name='update_Attendance'),
    
    
    path('create_Category/',views.create_Category,name='create_Category'),
    path('list_Category/',views.list_Category,name='list_Category'),
    path('delete_category/<int:id>/',views.delete_category,name='delete_category'),
    path('update_Category/<int:id>/',views.update_Category,name='update_Category'),
    path('list_payments/',views.list_payments,name='list_payments'),
]