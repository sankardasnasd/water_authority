"""
URL configuration for Water_authority project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),
    path('mainhome/',views.mainhome),

#________ADMIN______________________________________________________________________

    path('adminhome/',views.adminhome),

    path('Add_area/',views.Add_area),
    path('Add_area_post/', views.Add_area_post),

    path('View_area/', views.View_area),
    path('View_area_post/', views.View_area_post),

    path('district_add/', views.district_add),
    path('View_District/', views.View_District),
    path('district_add_post/', views.district_add_post),
    path('delete_District/<id>', views.delete_District),





    path('Edit_area/<id>', views.Edit_area),
    path('Edit_area_post/', views.Edit_area_post),
    path('delete_area/<id>', views.delete_area),


    path('Add_meter_reader/',views.Add_meter_reader),
    path('Add_meter_reader_post/', views.Add_meter_reader_post),

    path('View_meter_reader/', views.View_meter_reader),
    path('View_meter_reader_post/', views.View_meter_reader_post),

    path('edit_meter_reader/<id>', views.edit_meter_reader),
    path('edit_meter_reader_post/', views.edit_meter_reader_post),
    path('delete_meter_reader/<id>', views.delete_meter_reader),

    path('Admin_add_Charge/', views.Admin_add_Charge),
    path('Admin_add_Charge_post/', views.Admin_add_Charge_post),

    path('admin_edit_charge/<id>', views.admin_edit_charge),
    path('admin_edit_charge_post/', views.admin_edit_charge_post),

    path('delete_charge/<id>', views.delete_charge),

    path('admin_view_charge/', views.admin_view_charge),

    # path('view_new_conn_report/', views.view_new_conn_report),
    # path('view_new_conn_report_post/', views.view_new_conn_report_post),
    #
    # path('view_new_conn_report_post/', views.view_new_conn_report_post),

    path('admin_view_connection/', views.admin_view_connection),
    path('admin_view_connection_post/', views.admin_view_connection_post),

    path('admin_view_connection_approve/<id>', views.admin_view_connection_approve),
    path('admin_connection_reject/<id>', views.admin_connection_reject),

    path('admin_view_approved_connection/', views.admin_view_approved_connection),
    path('admin_view_approved_connection_post/', views.admin_view_approved_connection_post),

    path('admin_view_rejected_connections/', views.admin_view_rejected_connections),
    path('admin_view_rejected_connections_post/', views.admin_view_rejected_connections_post),

    path('admin_view_deactive_connection/', views.admin_view_deactive_connection),
    path('admin_view_deactive_connection_post/', views.admin_view_deactive_connection_post),

    path('Assign_meter_reader_get/', views.Assign_meter_reader_get),
    path('Assign_meter_reader_post/', views.Assign_meter_reader_post),

    path('View_assigned_mtr_reader/', views.View_assigned_mtr_reader),
    path('View_assigned_mtr_reader_post/', views.View_assigned_mtr_reader_post),

    path('Edit_assigned_meter_readers/<id>', views.Edit_assigned_meter_readers),
    path('Edit_assigned_meter_readers_post/', views.Edit_assigned_meter_readers_post),

    path('delete_assigned_meter_reader/<id>', views.delete_assigned_meter_reader),


    path('view_notification/', views.admin_view_notification),
    path('view_notification_post/', views.view_notificationsearch_post),

    path('Notification_send/', views.Notification_send),
    path('Notification_send_post/', views.Notification_send_post),

    path('Edit_notification/<did>', views.Edit_notification),
    path('Edit_notification_post/', views.Edit_notification_post),
    path('delete_notification/<id>', views.delete_notification),

    path('view_complaint/', views.view_complaint),
    path('view_complaint_post/', views.view_complaint_post),

    path('complnt_reply_form/<id>', views.complnt_reply_form),
    path('complnt_reply_form_post/', views.complnt_reply_form_post),

    path('Change_password_admin/', views.Change_password_admin),
    path('Change_password_admin_post/', views.Change_password_admin_post),

    path('view_due_report/', views.view_due_report),
    path('view_due_report_post/', views.view_due_report_post),

    path('view_due_report_deactivate/<id>', views.view_due_report_deactivate),

    path('view_public_complaint/', views.view_public_complaint),
    path('view_public_complaint_post/', views.view_public_complaint_post),









#________METER READER________________________________________________________________________________
    path('readerhome/', views.readerhome),

    path('view_profile_reader/', views.view_profile_reader),

    path('view_assigned_area/', views.view_assigned_area),

    path('search_customer_usage_entry/<id>', views.search_customer_usage_entry),
    path('search_customer_usage_entry_post/', views.search_customer_usage_entry_post),

    path('Usage_entry/<id>', views.Usage_entry),
    path('Usage_entry_post/', views.Usage_entry_post),

    path('view_notification_meter/', views.view_notification),
    path('view_notification_post_meter/', views.view_notification_post),

    path('view_previous_meter_readings/', views.view_previous_meter_readings),
    path('view_previous_meter_readings_post/', views.view_previous_meter_readings_post),

    path('view_user_upload_readings/', views.view_user_upload_readings),
    path('view_user_upload_readings_post/', views.view_user_upload_readings_post),

    path('Change_pass_meter/', views.Change_pass_meter),
    path('Change_pass_meter_post/', views.Change_pass_meter_post),

#_________USER_________________________________________________________________________________________

    path('userhome/', views.userhome),

    path('user_view_profile/', views.user_view_profile),

    path('edit_profile/', views.edit_profile),
    path('edit_profile_post/', views.edit_profile_post),

    path('new_bill_pay/', views.new_bill_pay),

    path('payment_form/<id>/<amnt>', views.payment_form),
    path('payment_form_post/', views.payment_form_post),

    path('view_montly_bill/', views.view_montly_bill),
    path('view_montly_bill_post/', views.view_montly_bill_post),

    path('user_upload/', views.user_upload),
    path('user_upload_post/', views.user_upload_post),

    path('Sent_complaint/', views.Sent_complaint),
    path('complaintform/<id>', views.complaintform),
    path('complaintform_post/', views.complaintform_post),




    path('user_change_pass/', views.user_change_pass),
    path('user_change_pass_post/', views.user_change_pass_post),



#________PUBLIC________________________________________________________________________________________________________
    path('New_conn/', views.New_conn),
    path('New_conn_post/', views.New_conn_post),

    path('New_conn_payment/', views.New_conn_payment),

    path('New/', views.New_conn_payment),

    path('pub_complaint_sent/', views.pub_complaint_sent),
    path('pub_complaint_sent_post/', views.pub_complaint_sent_post),

    path('forget_pass/', views.forget_pass),
    path('forget_pass_post/', views.forget_pass_post),


]
