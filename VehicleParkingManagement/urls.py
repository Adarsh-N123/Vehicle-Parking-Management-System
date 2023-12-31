"""VehicleParkingManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from vehicle.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('admin_home',admin_home,name='admin_home'),
    path('logout',Logout,name='logout'),
    path('changepassword',changepassword,name='changepassword'),
    path('search',search,name='search'),
    #path('add_category',add_category,name='add_category'),
    #path('manage_category',manage_category,name='manage_category'),
    #path('delete_category/<int:pid>', delete_category,name='delete_category'),
    path('add_vehicle',add_vehicle,name='add_vehicle'),
    path('manage_incomingvehicle',manage_incomingvehicle,name='manage_incomingvehicle'),
    path('view_incomingdetail/<int:pid>',view_incomingdetail,name='view_incomingdetail'),
    path('manage_outgoingvehicle',manage_outgoingvehicle,name='manage_outgoingvehicle'),
    path('view_outgoingdetail/<int:pid>',view_outgoingdetail,name='view_outgoingdetail'),
    path('print/<int:pid>',print_detail,name='print'),
    path('register',register,name='register'),
    #path('betweendate_report',betweendate_report,name='betweendate_report'),
    #path('betweendate_reportdetails',betweendate_reportdetails,name='betweendate_reportdetails'),
    #path('delete_event/<int:pid>',delete_event, name='delete-event'),
    path('delete/<int:pid>',delete_detail,name='delete'),
    path('show_slot_url/<int:parking_number>',show_slot_url,name='show_slot_url'),
    path('view_parking_map/<str:vechicleID>',view_parking_map,name='view_parking_map'),
    path('parking_map/<int:vechicleID>/<int:slotID>',booked_parking_map,name='parking_map'),
    path('update_slot/<int:vechicleID>/<int:slotID>',update_slot,name='slot_update'),
    path('monthly_bills',monthly_bills,name='monthly_bills'),
    path('view_monthly_bills/<str:month>',view_monthly_bills,name='view_monthly_bills'),
    path('changegrid',changegrid,name='changegrid'),
    path('enable_disable/<str:opcode>',enable_disable,name='enable_disable'),
    path('increase',increase,name='increase'),
    path('decrease',decrease,name='decrease'),


    

]
