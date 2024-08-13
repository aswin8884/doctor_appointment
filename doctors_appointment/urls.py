from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index),
    path('user_registration',views.user_registration),
    path('login',views.login),
    path('admin_home',views.admin_home),

    ################### ADMIN PAGES #####################
    path('add_doctors_admin',views.add_doctors_admin),
    path('view_doctors_admin',views.view_doctors_admin),
    path('view_doctor_admin_single',views.view_doctor_admin_single),
    path('update_doctor_admin',views.update_doctor_admin),
    path('delete_doctor_admin',views.delete_doctor_admin),
    path('view_users_admin',views.view_users_admin),
    path('view_user_admin_single',views.view_user_admin_single),
    path('delete_user_admin',views.delete_user_admin),
    path('view_complaints_admin',views.view_complaints_admin),
    path('reply_complaint_admin',views.reply_complaint_admin),

    ################### DOCTOR PAGES #####################
    path('doctor_home',views.doctor_home),
    path('add_appointment_doctor',views.add_appointment_doctor),
    path('view_appointment_doctor',views.view_appointment_doctor),
    path('view_profile_doctor',views.view_profile_doctor),
    path('edit_profile_doctor',views.edit_profile_doctor),
    path('view_bookings_doctor',views.view_bookings_doctor),
  
    ################### USER PAGES #####################
    path('user_home',views.user_home),
    path('view_slotes_user',views.view_slotes_user),
    path('payment_user',views.payment_user),
    path('view_bookings_user',views.view_bookings_user),
    path('cancel_appointment_user',views.cancel_appointment_user),
    path('view_doctors_user',views.view_doctors_user),
    path('add_complaints_user',views.add_complaints_user),
    path('view_complaints_user',views.view_complaints_user),
    path('add_feedbacks_user',views.add_feedbacks_user),
    path('view_feedbacks_user',views.view_feedbacks_user),
    path('view_profile_user',views.view_profile_user),
    path('edit_profile_user',views.edit_profile_user),
]
