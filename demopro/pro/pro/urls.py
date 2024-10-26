"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('about',views.about),
    path('services',views.services),
    path('contact',views.contact),
    path('signup',views.signup),
    path('login',views.login),
    path('userprofile',views.userprofile),
    path('userhome',views.userhome),
    path('userservice', views.userservice),
    path('singles/<int:id>', views.singles),
    path('booking', views.booking),
    path('a_send_bk.data/<int:id>', views.a_send_bk),
    path('cancelbookings/<int:id>', views.cancelbookings),
    path('admincancelbookings/<int:id>', views.admincancelbookings),
    path('finishedwork/<int:id>', views.finishedwork),
    path('viewfinishedwork', views.viewfinishedwork),

    path('u_c_bookings', views.u_cancelledbookings),
    path('admin_c_booking', views.admin_c_booking),
    path('usercontact', views.usercontact),
    path('userabout', views.userabout),
    path('adminhome', views.adminhome),
    path('adminviewuser', views.adminviewuser),
    path('addservice', views.addservices),
    path('addlocation', views.addlocation),
    path('viewlocation', views.viewlocation),
    path('viewbooking', views.viewbooking),
    path('d_viewbooking', views.d_viewbooking),
    path('driverreg', views.driverregistration),
    path('driverlogin', views.driverlogin),
    path('driverhome', views.driverhome),
    path('viewdrivers', views.viewdrivers),
    path('viewservice', views.viewservice),
    path('driverprofile', views.driverprofile),
    path('adminservice', views.adminservice),
    path('complaints', views.complaints),
    path('u_booking', views.u_bookings),
    path('refund_status/<int:id>', views.refund_status),
    path('statusup/<int:id>',views.statusupd),
    path('statusupd2',views.empstatusupd),
    # path('w_statusupd/<int:id>',views.wr_statusupd),
    path('wr_confirm/<int:id>',views.wr_confirm),
    path('updpr/<int:id>',views.updpr),
    path('profileupd/<int:id>',views.profileupd),
    path('razor',views.payment),
    path('refundpayment',views.refundpayment),
    path('razorpay/<int:price>/<int:pk>',views.razorpay),
    path('refund_razorpay/<int:totalprices>/<int:pk>', views.refund_razorpay),
    path('refundsuccess/<int:id>', views.refundsuccess),
    path('success/<int:id>',views.success),
    path('paymentstatus/<int:id>',views.paymentstatus),
    path('updateservice/<int:id>', views.updateservice),
    path('driver_confirm/<int:id>', views.driver_confirm),
    path('upd/<int:id>', views.updservice),
    path('delet_s/<int:id>', views.deleteservice),
    path('delet_l/<int:id>', views.deletelocation),
    path('delet_d/<int:id>', views.deletedrivers),
    path('delet_u/<int:id>', views.deleteuser),
    path('delet_b/<int:id>', views.deletebooking),
    path('delet_u_b/<int:id>', views.deleteu_booking),
    path('delet_d_vb/<int:id>', views.deletead_booking),
    path('delet_complaint/<int:id>', views.deletecomplaint),
    path('showcomplaints', views.showcomplaints),
    path('forgotpassword', views.forgot_password),
    path('reset/<token>', views.resetpassword),
    path('logout', views.logout),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)