from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import *
# from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your views here.



def home(re):
    return render(re,'Home.html')
def about(re):
    return render(re,'about.html')
def services(re):
    data = add_service.objects.all()
    return render(re, "services.html", {'a': data})

    return render(re, 'services.html')
def contact(request):

    return render(request, 'contact.html')
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password != cpassword:
            messages.error(request, "password do not match")
            return render(request, "signup.html")
        if register.objects.filter(username=username).exists():
            messages.error(request,"Already Existing User")
            return redirect(signup)
        if register.objects.filter(phonenumber=phonenumber).exists():
            messages.error(request, "Already Existing Phone number")
            return redirect(signup)
        if register.objects.filter(email=email).exists():
            messages.error(request, "Already Existing Email")
            return redirect(signup)

        else:
            d=register(username=username, email=email,address=address,phonenumber=phonenumber,password=password,cpassword=cpassword)
            d.save()
            messages.success(request,"Profile created")
    return render(request,"signup.html")
def login(request):
    if request.method == 'POST':
        users = request.POST['users']
        passw = request.POST['passw']
        try:
            data = register.objects.get(username=users)
            if users == data.username and passw == data.password:
                request.session['id'] = users
                return redirect(userhome)
            else:
                messages.error(request, 'Invalid Username or Password')
        except Exception:
            if users == 'admin' and passw == 'admin':
                request.session['id1'] = users
                return redirect(adminhome)
            else:
                messages.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')
def driverregistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        b = request.POST['email']
        profile = request.FILES['profilepic']
        cv = request.FILES['img1']
        c = request.POST['phonenumber']
        z = request.POST['gender']
        e = request.POST['address']
        f = request.POST['joiningdate']
        g = request.POST['licensenumber']
        i = request.POST['location']
        password = request.POST['password']
        c_password = request.POST['c_password']

        # Password check
        if password != c_password:
            messages.error(request, "Password do not match")
            return render(request, "driversignup.html")

        # Check if driver already exists
        if driverreg.objects.filter(name=name).exists():
            messages.error(request, "Already Existing")
            return render(request, "driversignup.html")
        if driverreg.objects.filter(location=i).exists():
            messages.error(request, "Already Existing Location")
            return render(request, "driversignup.html")
        if driverreg.objects.filter(email=b).exists():
            messages.error(request, "Already Existing Email")
            return render(request, "driversignup.html")
        if driverreg.objects.filter(phonenumber=c).exists():
            messages.error(request, "Already Existing Phone Number")
            return render(request, "driversignup.html")
        if driverreg.objects.filter(licensenumber=g).exists():

            messages.error(request, "Already Existing License Number")
            return render(request, "driversignup.html")
        else:
            # Save driver details
            d = driverreg(
                name=name,
                email=b,
                profile=profile,
                cv=cv,
                phonenumber=c,
                gender=z,
                address=e,
                joiningdate=f,
                licensenumber=g,
                location=i,
                password=password,
                c_password=c_password
            )
            d.save()
            messages.success(request, "Profile created")

    # Fetch locations to pass into the template
    location = add_location.objects.all()

    # Render the registration template with the fetched data
    return render(request, "driversignup.html", {'loc': location})


def userprofile(request):
    if "id" in request.session:
        a=register.objects.get(username=request.session['id'])
        return render(request, "userprofile.html",{'data':a})
    return redirect(login)
def userhome(re):
    return render(re, "userhome.html")
def userservice(re):
    data = add_service.objects.all()
    return render(re, "userservice.html",{'a':data})

    # ------------------------user details fetching code ----------------------->
def singles(request,id):
    if 'id' in request.session:
        user = register.objects.get(username=request.session['id'])
        if user:
            service = add_service.objects.get(pk=id)
            location = add_location.objects.all()
            return render(request, 'booking.html', {'a': user, 'pdata': service,'loc':location})
    return redirect(userservice)

def booking(request):
    if request.method== 'POST':
        a = request.POST['name']
        c = request.POST['email']
        s = request.POST['type']
        p = request.POST['phonenumber']
        e = request.POST['address']
        price = request.POST['price']
        pickingpoint  = request.POST['pickingpoint']
        q = request.POST['quantity']
        totalprices = request.POST['totalprices']
        f = request.POST['pickingdate']
        h = request.POST['location']
        district = request.POST['district']
        state = request.POST['state']

        data = bookings.objects.create(name=a,email=c, type=s,price=price,phonenumber=p,address=e, pickingdate=f,location=h,
                                       pickingpoint=pickingpoint,quantity=q,totalprices=totalprices,district=district,
                                       state=state)
        data.save()
        return redirect(u_bookings)
        return render(request, "booking.html")
    else:
       return render(request, "booking.html")

def u_bookings(request):
    if 'id' in request.session:
        # Fetch the current user from the session
        user = register.objects.get(username=request.session['id'])

        # Get all bookings made by the current user
        user_bookings = bookings.objects.filter(name=user.username)

        # Fetch all work status from adminsendbookings
        work_status_list = adminsendbookings.objects.all()

        # Create a set of booked IDs for payment status checking
        book_ids = set(booked.objects.values_list('id', flat=True))
        finishedbooking = set(finishedworks.objects.values_list('id', flat=True))

        # Map each booking with its corresponding work status and payment status
        for booking in user_bookings:
            # try:
            #     # Get work status for each booking
            #     booking_work_status = work_status_list.get(id=booking.id)
            #     booking.cl_status = booking_work_status.cl_status
            # except adminsendbookings.DoesNotExist:
            #     booking.w_status = 'Pending'

            # Determine payment status for each booking
            if booking.id in book_ids:
                booking.payment_status = 'cash paid'
            else:
                booking.payment_status = 'cash not paid'

            # Update the payment status in the database (if needed)
            bookings.objects.filter(id=booking.id).update(payment_status=booking.payment_status)
            if booking.id in finishedbooking:
                booking.w_status = 'Finished'
            else:
                booking.w_status = 'Pending'
            bookings.objects.filter(id=booking.id).update(w_status=booking.w_status)
        # Pass bookings with work status and payment status to the template
        return render(request, "u_bookings.html", {
            'bk': user_bookings,
            'c': booked.objects.all(),  # Assuming you still want to pass this
        })

    # If user is not logged in, redirect or render an empty bookings page
    return render(request, "u_bookings.html", {})


def cancelbookings(request,id):
    # if 'id' in request.session:
    data=bookings.objects.filter(pk=id)
    book=data.first()
    datas = adminsendbookings.objects.filter(pk=id)
    # books = datas.first()
    a = cancelbooking.objects.create(
        id=book.id,
        name=book.name,
        email=book.email,
        type=book.type,
        quantity=book.quantity,
        totalprices=book.price,
        phonenumber=book.phonenumber,
        address=book.address,
        pickingdate=book.pickingdate,
        location=book.location,
        district=book.district,
        state=book.state,
        pickingpoint=book.pickingpoint
    )
    a.save()
    data.delete()
    datas.delete()

    # Display success message and redirect
    messages.success(request, 'Booking Cancelled')
    return redirect(u_bookings)

def admincancelbookings(request,id):
    # if 'id' in request.session:
    data=bookings.objects.filter(pk=id)
    book=data.first()
    datas = adminsendbookings.objects.filter(pk=id)
    # books = datas.first()
    a = cancelbooking.objects.create(
        id=book.id,
        name=book.name,
        email=book.email,
        type=book.type,
        quantity=book.quantity,
        totalprices=book.price,
        phonenumber=book.phonenumber,
        address=book.address,
        pickingdate=book.pickingdate,
        location=book.location,
        district=book.district,
        state=book.state,
        pickingpoint=book.pickingpoint
    )
    a.save()
    data.delete()
    datas.delete()

    # Display success message and redirect
    messages.success(request, 'Booking Cancelled')
    return redirect(viewbooking)
def u_cancelledbookings(request):
    if 'id' in request.session:
        # Fetch the current user from the session
        user = register.objects.get(username=request.session['id'])

        # Get all bookings made by the current user
        user_bookings = bookings.objects.filter(name=user.username)
        c_bookings = cancelbooking.objects.filter(name=user.username)


        # Create a set of booked IDs for payment status checking
        book_ids = set(booked.objects.values_list('id', flat=True))
        refund_s = set(cancelsucces.objects.values_list('id', flat=True))

        # Map each booking with its corresponding work status and payment status
        for booking in c_bookings:
            # Determine payment status for each booking
            if booking.id in book_ids:
                booking.payment_status = 'cash paid'
            else:
                booking.payment_status = 'cash not paid'

            # Update the payment status in the database (if needed)
            bookings.objects.filter(id=booking.id).update(payment_status=booking.payment_status)
            if booking.id in refund_s:
                booking.refund_status = "Cash refunded"
            else:
                booking.refund_status = ""


            cancelbooking.objects.filter(id=booking.id).update(refund_status=booking.refund_status)



        # Pass bookings with work status and payment status to the template
        return render(request, "cancelledbookings.html", {
            'c': c_bookings,
            'bk': booked.objects.all(),  # Assuming you still want to pass this
        })

        # If user is not logged in, redirect or render an empty bookings page
    return render(request, "cancelledbookings.html", {})


def a_send_bk(request,id):
    data=bookings.objects.filter(pk=id)
    book=data.first()
    a = adminsendbookings.objects.create(
        id=book.id,
        name=book.name,
        email=book.email,
        type=book.type,
        quantity=book.quantity,
        price=book.price,
        phonenumber=book.phonenumber,
        address=book.address,
        pickingdate=book.pickingdate,
        city=book.location,
        landmark=book.pickingpoint,
        district=book.district,
        state=book.state,


    )

    # Save the new entry
    a.save()

    # Display success message and redirect
    messages.success(request, 'Work sent successfully.')
    return redirect(viewbooking)


def d_viewbooking(request):
    # if 'empid'in request.session:
    #     user= driverreg.objects.get(name=request.session['empid'])
    #     data = adminsendbookings.objects.filter(city=user.location)
    #     return render(request, "driverviewbooking.html", {'da':data,'c':user})

    if 'empid' in request.session:
        user = driverreg.objects.get(name=request.session['empid'])

        # Fetch the data based on the user's location
        data = adminsendbookings.objects.filter(city=user.location)

        # Update emp_status to "In work" only if there is data
        if data.exists():
            driverreg.objects.filter(name=user.name).update(emp_status="In work")
        else:
            driverreg.objects.filter(name=user.name).update(emp_status="Free")

        return render(request, "driverviewbooking.html", {'da': data, 'c': user})

    return render(request, "driverviewbooking.html")





def forgot_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        try:
            user=register.objects.get(email=email)
        except register.DoesNotExist:
            user=None
        try:
            emp=driverreg.objects.get(email=email)
        except driverreg.DoesNotExist:
            emp=None
        if not user and not emp:
            messages.info(request,'Email is not Registered')
            # return redirect('forgot_password')
        if user:
            token=get_random_string(length=4)
            passwordreset.objects.create(users=user,token=token)
            messages.info(request, 'Link is sent to your Registered Email')
        else:
            token=get_random_string(length=4)
            passwordreset.objects.create(emp=emp,token=token)
            messages.info(request, 'Link is sent to your Registered Email')
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset your password',f'Click the link to reset your password:{reset_link}',
                      'settings.EMAIL_HOST_USER',[email],fail_silently=False)
        except:
            # messages.info(request,'Network connection failed')
            return redirect(forgot_password)
    return render(request,"forgotpassword.html")

def resetpassword(request,token):
    print(token)
    password_reset=passwordreset.objects.get(token=token)
    if request.method=='POST':
        new_password=request.POST.get('newpassword')
        repeat_password=request.POST.get('cpassword')
        if repeat_password == new_password:
            try:
                password_reset.users.password = new_password
                password_reset.users.save()
                messages.info(request, 'Password Reset Successfully')
            except:
                password_reset.emp.password = new_password
                password_reset.emp.save()
                messages.info(request, 'Password Reset Successfully')
            return redirect(login)
        messages.info(request, 'New password and Confirm Password is not matching')

        return render(request,'resetpassword.html',{'token':token})



    return render(request, "resetpassword.html")

def usercontact(request):
    if 'id' in request.session:
        user = register.objects.get(username=request.session['id'])
    return render(request, "usercontact.html",{'user':user})
def userabout(re):
    return render(re, "userabout.html")
def adminhome(re):
    return render(re, "adminhome.html")
def adminviewuser(request):

    d = register.objects.all()
    return render(request, "adminviewuser.html", {'a': d})

def viewbooking(request):

    # if 'id' in request.session:
        # Retrieve all bookings, drivers, and admin bookings
    bookings_list = bookings.objects.all()
    drivers = driverreg.objects.all()
    work_status_list = adminsendbookings.objects.all()

    # Create a set of booked IDs to check for payment status
    book_ids = set(booked.objects.values_list('id', flat=True))
    finishedbooking = set(finishedworks.objects.values_list('id', flat=True))

    for booking in bookings_list:
        try:
            # Get work status and confirmation for each booking
            booking_work_status = work_status_list.get(id=booking.id)
            booking.cl_status = booking_work_status.cl_status
            booking.w_confirm = booking_work_status.w_confirm
        except adminsendbookings.DoesNotExist:
            booking.w_status = 'Pending'
            booking.w_confirm = 'Pending'

        # Determine payment status and update each booking object
        if booking.id in book_ids:
            booking.payment_status = 'cash paid'
        else:
            booking.payment_status = 'cash not paid'

        # Update the payment status in the database (optional, if needed)
        bookings.objects.filter(id=booking.id).update(payment_status=booking.payment_status)
        if booking.id in finishedbooking:
            booking.w_status = 'Finished'
        else:
            booking.w_status = 'Pending'
        bookings.objects.filter(id=booking.id).update(w_status=booking.w_status)

    # Render the view with the updated bookings_list and drivers data
    return render(request, "viewbooking.html", {
        'a': bookings_list,
        'data': drivers,
    })

    return redirect(adminhome)

def admin_c_booking(request):
    c_booking = cancelbooking.objects.all()

    # Create a set of booked IDs to check for payment status
    book_ids = set(booked.objects.values_list('id', flat=True))
    refund_s = set(cancelsucces.objects.values_list('id', flat=True))

    for booking in c_booking:

        # Determine payment status and update each booking object
        if booking.id in book_ids:
            booking.payment_status = 'cash paid'
        else:
            booking.payment_status = 'cash not paid'

        # Update the payment status in the database (optional, if needed)
        bookings.objects.filter(id=booking.id).update(payment_status=booking.payment_status)
        if booking.id in refund_s:
            booking.refund_status = "Cash refunded"
        else:
            booking.refund_status = ""

        cancelbooking.objects.filter(id=booking.id).update(refund_status=booking.refund_status)


    # Render the view with the updated bookings_list and drivers data
    return render(request, "a_cancelledbookings.html", {
        'a': c_booking,
    })

    # Redirect to login if the user is not logged in
    return redirect(viewbooking)


def addservices(request):
    if request.method == 'POST':
        a = request.POST['type']
        b = request.POST['price']
        c = request.FILES['image']
        data = add_service.objects.create(type=a, price=b,image=c)
        data.save()
        return redirect(viewservice)
    else:
        return render(request, "addservice.html")

def addlocation(request):
    if request.method == 'POST':
        a = request.POST['location']
        data = add_location.objects.create(location=a)
        data.save()
        return redirect(viewlocation)
    else:
        return render(request, "addlocation.html")

def driverlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        # try:

        data = driverreg.objects.get(name=name)
        if data.c_status == "Accepted":
            if name == data.name and password == data.password:
                request.session['empid'] = name
                return redirect(driverhome)
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Admin is not Accepted Your Registration')

    return render(request, "driverlogin.html")
def driverhome(re):
    return render(re, "drivershome.html")
def driverprofile(request):
    if "empid" in request.session:
        d = driverreg.objects.get(name=request.session['empid'])
        return render(request, "driverprofile.html",{'a': d})
    return redirect(driverlogin)
    # return render(request, "driverprofile.html")
def viewdrivers(request):
    d = driverreg.objects.all()
    return render(request, "viewdrivers.html", {'a': d,})

def viewservice(request):
    d = add_service.objects.all()
    return render(request, "viewservice.html", {'a': d})
def viewlocation(request):
    d = add_location.objects.all()
    return render(request, "viewlocation.html", {'a': d})
def adminservice(request):
    return render(request,"adminservice.html")
def updservice(re,id):
    data=add_service.objects.get(pk=id)
    return render(re,'updateservice.html',{'updata':data})
def updateservice(re,id):
    if re.method=="POST":
        a=re.POST['type']
        b=re.POST['price']

        add_service.objects.filter(pk=id).update(type=a,price=b)
        return redirect(viewservice)
    else:
        return render(re,"updateservice.html")
def updpr(request,id):
    data = register.objects.get(pk=id)
    return render(request, 'updateprofile.html', {'updata': data})
def profileupd(request,id):
    if request.method=="POST":
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['phonenumber']
        d = request.POST['address']

        register.objects.filter(pk=id).update(username=a,email=b,phonenumber=c,address=d)
        messages.success(request, "Profile Updated successfully")
        return redirect(userprofile)
    else:
        return render(request,"userprofile.html")


def refund_status(request,id):
    if request.method == "POST":
        a = request.POST['status']
        cancelbooking.objects.filter(id=id).update(r_status=a)
        return redirect(admin_c_booking)
    else:
        return render(request, "a_cancelledbooking.html")
def statusupd(request,id):
    if request.method == "POST":
        a = request.POST['status']
        bookings.objects.filter(id=id).update(status=a)
        return redirect(viewbooking)
    else:
        return render(request, "viewbooking.html")



def empstatusupd(request):
    if request.method == "POST":
        if 'empid' in request.session:
            u = driverreg.objects.get(name=request.session['empid'])
            a = request.POST['status']
            driverreg.objects.filter(name=u.name).update(emp_status=a)
            return redirect(driverprofile)
    else:
        return render(request, "driverviewbooking.html")

def driver_confirm(request,id):
    if request.method == "POST":
        a = request.POST['status']
        driverreg.objects.filter(id=id).update(c_status=a)
        return redirect(viewdrivers)

    else:
        return render(request, "viewdrivers.html")


def wr_statusupd(request,id):
    if request.method == "POST":
        a = request.POST['cl_status']
        adminsendbookings.objects.filter(id=id).update(cl_status=a)
        return redirect(d_viewbooking)
    else:
        return render(request, "driverviewbooking.html")

def wr_confirm(request,id):
    if request.method == "POST":
        a = request.POST['wr_confirm']
        adminsendbookings.objects.filter(id=id).update(w_confirm=a)
        return redirect(d_viewbooking)

    else:
        return render(request, "driverviewbooking.html")

def paymentstatus(request,id):
    if request.method == "POST":
        # if 'id' in request.session:
        #     u = register.objects.get(username=request.session['id'])
            a = request.POST['p_status']
            bookings.objects.filter(id=id).update(p_status=a)
            # bookings.objects.filter(name=u.username).update(p_status=a)
            return redirect(u_bookings)
    else:
        return render(request,"u_bookings.html")

def deleteservice(request,id):
    data=add_service.objects.get(pk=id)
    data.delete()
    return redirect(viewservice)
def deletelocation(request,id):
    data=add_location.objects.get(pk=id)
    data.delete()
    return redirect(viewlocation)
def deletedrivers(request,id):
    data=driverreg.objects.get(pk=id)
    data.delete()
    return redirect(viewdrivers)
def deleteuser(request,id):
    data = register.objects.get(pk=id)
    data.delete()
    return redirect(adminviewuser)
def deletebooking(request,id):
    data = bookings.objects.get(pk=id)
    data.delete()
    return redirect(viewbooking)
def deleteu_booking(request,id):
    data = bookings.objects.get(pk=id)
    data.delete()
    return redirect(u_bookings)
def deletead_booking(request,id):
    data = adminsendbookings.objects.get(pk=id)
    data.delete()
    return redirect(d_viewbooking)
def deletecomplaint(request,id):
    data = complaint.objects.get(pk=id)
    data.delete()
    return redirect(showcomplaints)
def payment(request):
    return render(request, "razor.html")
def refundpayment(request):
    return render(request, "refundrazor.html")
def razorpay(request,price,pk):
    if 'id' in request.session:
        u=register.objects.get(username=request.session['id'])
        c=bookings.objects.filter(name=u)
        p=price*100
        return render(request,'razor.html',{'amount':p,'pk':pk})
    return redirect(payment)

def refund_razorpay(request,totalprices,pk):
    if 'id' in request.session:
        u=register.objects.get(username=request.session['id'])
        c=cancelbooking.objects.filter(name=u)
        p=totalprices*100
        return render(request,'refundrazor.html',{'amount':p,'pk':pk})
    return redirect(refundpayment)
def refundsuccess(request,id):
    book = cancelbooking.objects.get(pk=id)
    c = cancelsucces.objects.create(
        id=book.id,
        name=book.name, email=book.email, type=book.type, phonenumber=book.phonenumber,
        address=book.address, pickingdate=book.pickingdate, location=book.location, pickingpoint=book.pickingpoint,
        quantity=book.quantity, totalprices=book.totalprices
    )
    c.save()
    return render(request, "refundsuccess.html")

def success(request,id):
    book=bookings.objects.get(pk=id)
    c = booked.objects.create(
        id=book.id,
        name=book.name,email=book.email, type=book.type,price=book.price,phonenumber=book.phonenumber,address=book.address, pickingdate=book.pickingdate,location=book.location,pickingpoint=book.pickingpoint,quantity=book.quantity,totalprices=book.totalprices
    )
    c.save()
    return render(request, "success.html")
def complaints(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data=complaint.objects.create(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request, "Complaint Registered successfully")
    return redirect(usercontact)
    # return render(request,"usercontact.html")
def showcomplaints(request):
    data=complaint.objects.all()
    return render(request,"showcomplaint.html",{'data':data})
def logout(request):
    request.session.flush()
    return redirect(home)

def finishedwork(request,id):
    data = adminsendbookings.objects.filter(pk=id)
    books = data.first()
    a = finishedworks.objects.create(
        id=books.id,
        name=books.name,
        email=books.email,
        type=books.type,
        quantity=books.quantity,
        price=books.price,
        phonenumber=books.phonenumber,
        address=books.address,
        pickingdate=books.pickingdate,
        city=books.city,
        district=books.district,
        state=books.state,
        landmark=books.landmark
    )
    a.save()
    data.delete()
    messages.success(request, 'Booking Finished')
    # data.delete()
    return redirect(d_viewbooking)
def viewfinishedwork(request):
    if 'empid' in request.session:
        a = driverreg.objects.get(name=request.session['empid'])
        b = finishedworks.objects.filter(city=a.location)
        return render(request, "viewfinishedwork.html", {'b': b, 'cc': a})
