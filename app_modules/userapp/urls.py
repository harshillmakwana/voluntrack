from django.contrib import admin
from django.urls import path,include
from app_modules.userapp import views


urlpatterns = [
    path('myname/',views.myname,name='myname'),
    
    # template file 
    path('about_view1',views.about_view,name ="about_view1"),
    path('contact_view1',views.contact_view,name ="contact_view1"),
    path('dashboard_view',views.dashboard_view,name ="dashboard_view"),
    path('events_view1',views.events_view,name ="events_view1"),
    path('',views.index_view,name ="index_view1"),
    
    path('volunteer_register/', views.volunteer_register, name='volunteer_register'),
    path('organizer_register/', views.organizer_register, name='organizer_register'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('user_profile/', views.user_profile, name='user_profile'),
    
    # path("create-admin/", views.create_admin, name="create_admin"),
    path("check-admin/", views.check_admin),
    path('volunteers_view1',views.volunteers_view,name ="volunteers_view1"),
    
    # models
    # path('create_CustomUser/',views.create_CustomUser,name="create_CustomUser"),
    
    
    # Authentication Views
    path('org_dashboard/', views.org_dashboard, name='org_dashboard'),
    
    path('org_dahs_create_category/', views.org_dahs_create_category, name='org_dahs_create_category'),
    path('org_dash_categoryevent/', views.org_dash_categoryevent, name='org_dash_categoryevent'),
    path('delete_org_categoryevent/<int:id>/', views.delete_org_categoryevent, name='delete_org_categoryevent'),
    path('update_org_Category/<int:id>/', views.update_org_Category, name='update_org_Category'),
    
    path('org_dash_create_event/', views.org_dash_create_event, name='org_dash_create_event'),
    path('org_dash_event/', views.org_dash_event, name='org_dash_event'),
    path('delete_org_event/<int:id>/', views.delete_org_event, name='delete_org_event'),
    path('update_org_event/<int:id>/', views.update_org_event, name='update_org_event'),
    
    path('org_dash_create_VolunteerApplication/', views.org_dash_create_VolunteerApplication, name='org_dash_create_VolunteerApplication'),
    path('org_dash_voleteer/', views.org_dash_voleteer, name='org_dash_voleteer'),
    path('delete_org_voleteer/<int:id>/', views.delete_org_voleteer, name='delete_org_voleteer'),
    path('update_org_VolunteerApplication/<int:id>/', views.update_org_VolunteerApplication, name='update_org_VolunteerApplication'),
    
    path('create_booking/', views.create_booking, name='create_booking'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('create_booking/<int:id>/', views.create_booking, name='create_booking'),
    path('org_booking_show/', views.org_booking_show, name='org_booking_show'),
    path('volunterr_event_show/', views.volunterr_event_show, name='volunterr_event_show'),
    
    path('approve_book/<int:id>/', views.approve_book, name='approve_book'),
    path('reject_book/<int:id>/', views.reject_book, name='reject_book'),
    
    path('org_profille/', views.org_profille, name='org_profille'),
    
    path('create_payment/', views.create_payment, name='create_payment'),
    path('create_payment/<int:id>/', views.create_payment, name='create_payment'),
    path('payment_history/', views.payment_history, name='payment_history'),
    path('update_process_status/<int:id>/<str:status>/', views.update_process_status, name='update_process_status'),
    path('invoice/<int:id>/', views.invoice_detail, name='invoice_detail'),
    path('submit_feedback/<int:id>/', views.submit_feedback, name='submit_feedback'),



  



path('chat/', views.chat_index, name='chat_index'),

path(
'chat_room/<int:id>/',
views.chat_room,
name='chat_room'
),

path(
'get-messages/<int:id>/',
views.get_messages,
name='get_messages'
),

path(
'send-message/<int:id>/',
views.send_message,
name='send_message'
),

path(
'delete-message/<int:id>/',
views.delete_message,
name='delete_message'
),

path(
'clear-chat/<int:id>/',
views.clear_chat,
name='clear_chat'
),

    
    
]  