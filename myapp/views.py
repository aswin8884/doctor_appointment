from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:

        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype == "user":
                    user=User_registration.objects.get(email=email)
                    request.session["email"]=email
                    request.session["id"]=user.id
                    return redirect('/user_home')
                elif user.usertype == "doctor":
                    user=Add_doctors.objects.get(email=email)
                    request.session["email"]=email
                    request.session["id"]=user.id
                    return redirect('/doctor_home')

    return render(request,"login.html")

def user_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']
        email=request.POST['email']
        password=request.POST['password']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(
            username=email,
            password=password,
            usertype="user"
        )
        log.save()
        
        regi=User_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            age=age,
            gender=gender,
            email=email,
            login_id=log,
            profile_picture=profile_picture
        )
        regi.save()
        messages.info(request,"Registration Successfull You Can Login Now")
        return redirect('/user_registration')

    return render(request,"user_registration.html")


######################### ADMIN PAGES ####################################

def admin_home(request):

    doctors=Add_doctors.objects.all()
    users=User_registration.objects.all()
    complaint=Add_complaints.objects.all()

    doctor_count=0
    user_count=0
    complaint_count=0
    
    for d in doctors:
        doctor_count+=1
        d.id
    for u in users:
        user_count+=1
        u.id
    for c in complaint:
        complaint_count+=1
        c.id

    return render(request,"admin/admin_home.html",
                  {
                    "doctor_count":doctor_count,
                    "user_count":user_count,
                    "complaint_count":complaint_count,
                    })

def add_doctors_admin(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        age=request.POST['age']
        gender=request.POST['gender']
        specialization=request.POST['specialization']
        hospital=request.POST['hospital']
        description=request.POST['description']
        experience=request.POST['experience']
        email=request.POST['email']
        password=request.POST['password']
        qualification=request.POST['qualification']
        profile_picture=request.FILES['profile_picture']


        log=Login_table.objects.create_user(username=email,password=password,usertype="doctor")
        log.save()

        doctor=Add_doctors.objects.create(
            name=name,
            contact=contact,
            address=address,
            age=age,
            gender=gender,
            specialization=specialization,
            hospital=hospital,
            description=description,
            experience=experience,
            email=email,
            qualification=qualification,
            profile_picture=profile_picture,
            login_id=log
        )
        doctor.save()
        messages.info(request,"Added Successfully")

    return render(request,"admin/add_doctors_admin.html")

def view_doctors_admin(request):

    doctors=Add_doctors.objects.all()

    return render(request,"admin/view_doctors_admin.html",{"doctors":doctors})

def view_doctor_admin_single(request):

    id=request.GET.get('id')

    doctor=Add_doctors.objects.get(id=id)

    return render(request,"admin/view_doctor_admin_single.html",{"doctor":doctor})

def update_doctor_admin(request):

    d_id=request.GET.get('id')
    doctor=Add_doctors.objects.get(id=d_id)

    if request.POST:
        name=request.POST['name']
        doctor.name=name
        contact=request.POST['contact']
        doctor.contact=contact
        age=request.POST['age']
        doctor.age=age
        gender=request.POST['gender']
        doctor.gender=gender
        address=request.POST['address']
        doctor.address=address
        qualification=request.POST['qualification']
        doctor.qualification=qualification
        experience=request.POST['experience']
        doctor.experience=experience
        hospital=request.POST['hospital']
        doctor.hospital=hospital
        specialization=request.POST['specialization']
        doctor.specialization=specialization
        description=request.POST['description']
        doctor.description=description
        profile_picture=request.FILES['profile_picture']
        doctor.profile_picture=profile_picture

        doctor.save()

        messages.info(request,"Updated Successfully")
        return redirect('/view_doctor_admin_single') 

    return render(request,"admin/update_doctor_admin.html",{"doctor":doctor})

def delete_doctor_admin(request):

    d_id=request.GET.get('id')
    doctor=Add_doctors.objects.get(id=d_id)
    doctor.delete()

    log=Login_table.objects.get(username=doctor.login_id)
    log.delete()

    messages.info(request,"Deleted successfully")

    return redirect('/view_doctors_admin')

def view_users_admin(request):

    users=User_registration.objects.all()

    return render(request,"admin/view_users_admin.html",{"users":users})

def view_user_admin_single(request):

    uid=request.GET.get('id')
    user=User_registration.objects.get(id=uid)

    return render(request,"admin/view_user_admin_single.html",{"user":user})

def delete_user_admin(request):

    uid=request.GET.get('id')
    u=User_registration.objects.get(id=uid)
    u.delete()
    log=Login_table.objects.get(username=u.login_id)
    log.delete()
    messages.info(request,"Removed Successfully")

    return redirect('/view_users_admin')

def view_complaints_admin(request):

    complaints=Add_complaints.objects.all()

    return render(request,"admin/view_complaints_admin.html",{"complaints":complaints})

def reply_complaint_admin(request):

    cid=request.GET.get('id')
    complaint=Add_complaints.objects.get(id=cid)

    if request.POST:
        reply=request.POST['reply']

        complaint.admin_reply=reply
        complaint.reply_date=timezone.now()
        complaint.save()
        messages.info(request,"Replied successfully")
        return redirect('/view_complaints_admin')

    return render(request,"admin/reply_complaint_admin.html")
######################### DOCTOR PAGES ###################################

def doctor_home(request):

    id=request.session['id']
    doctor=Add_doctors.objects.get(id=id)

    return render(request,"doctor/doctor_home.html",{"doctor":doctor})

def add_appointment_doctor(request):
    id = request.session['id']
    doctor = Add_doctors.objects.get(id=id)

    if request.method == 'POST':
        fees = request.POST['fees']
        appointment_time_from = request.POST['appointment_time_from']
        appointment_time_to = request.POST['appointment_time_to']
        appointment_date = request.POST['appointment_date']

        # Check if the appointment slot is already taken
        existing_appointment = Add_appointment.objects.filter(
            doctor_id=doctor,
            appointment_time_from=appointment_time_from,
            appointment_date=appointment_date,
        ).exists()

        if existing_appointment:
            messages.error(request, "The slot is already added by this date and time.")
            return redirect('/add_appointment_doctor')  

        # Create the appointment if the slot is available
        appointment = Add_appointment.objects.create(
            fees=fees,
            appointment_time_from=appointment_time_from,
            appointment_time_to=appointment_time_to,
            appointment_date=appointment_date,
            doctor_id=doctor
        )
        appointment.save()
        messages.success(request, "Added Successfully")
        return redirect('/add_appointment_doctor')

    return render(request, "doctor/add_appointment_doctor.html")

def view_appointment_doctor(request):
    # Get the current date and time
    current_time = timezone.now()
    date_filter = request.GET.get('date')
    id = request.session['id']

    # Get the doctor instance
    doctor = Add_doctors.objects.get(id=id)

    if date_filter:
        # If a specific date is filtered, only show slots for that date
        slotes = Add_appointment.objects.filter(appointment_date=date_filter, doctor_id=doctor)
    else:
        # Otherwise, filter for current and future appointments
        slotes = Add_appointment.objects.filter(
            doctor_id=doctor,
            appointment_date__gte=current_time.date()
        ).exclude(
            appointment_date=current_time.date(),
            appointment_time_to__lt=current_time.time()
        )

    return render(request, "doctor/view_appointment_doctor.html", {"slotes": slotes})

def view_profile_doctor(request):

    id = request.session['id']
    doctor=Add_doctors.objects.get(id=id)

    return render(request,"doctor/view_profile_doctor.html",{"doctor":doctor})

def view_bookings_doctor(request):
    id = request.session.get('id')
    if not id:
        return redirect('/login')

    doctor = Add_doctors.objects.get(id=id)
    
    date_filter = request.GET.get('date')
    if date_filter:
        try:
            date_filter = timezone.datetime.strptime(date_filter, '%Y-%m-%d').date()
            bookings = Booking_slote.objects.filter(slote_id__doctor_id=doctor, slote_id__appointment_date=date_filter).order_by('-slote_id__appointment_date')
        except ValueError:
            bookings = Booking_slote.objects.filter(slote_id__doctor_id=doctor).order_by('-slote_id__appointment_date')
    else:
        bookings = Booking_slote.objects.filter(slote_id__doctor_id=doctor).order_by('-slote_id__appointment_date')

    return render(request, "doctor/view_bookings_doctor.html", {"bookings": bookings})

def edit_profile_doctor(request):

    did=request.GET.get('id')
    doctor=Add_doctors.objects.get(id=did)
    if request.POST:
        name=request.POST['name']
        doctor.name=name
        address=request.POST['address']
        doctor.address=address
        contact=request.POST['contact']
        doctor.contact=contact
        age=request.POST['age']
        doctor.age=age
        hospital=request.POST['hospital']
        doctor.hospital=hospital
        description=request.POST['description']
        doctor.description=description
        experience=request.POST['experience']
        doctor.experience=experience
        profile_picture=request.FILES['profile_picture']
        doctor.profile_picture=profile_picture

        doctor.save()
        messages.info(request,"Updated Successfully")
        return redirect('/view_profile_doctor')
    return render(request,"doctor/edit_profile_doctor.html",{"doctor":doctor})

######################### USER PAGE ######################################

def user_home(request):

    id=request.session['id']
    user=User_registration.objects.get(id=id)

    return render(request,"user/user_home.html",{"user":user})

def view_slotes_user(request):
    current_time = timezone.now()
    date_filter = request.GET.get('date')

    if date_filter:
        try:
            # Convert the date_filter to a date object
            date_filter = timezone.datetime.strptime(date_filter, '%Y-%m-%d').date()
        except ValueError:
            # Handle the case where the date_filter is invalid
            date_filter = None

    if date_filter:
        slotes = Add_appointment.objects.filter(
            appointment_date=date_filter,
            user_booked=False,
            appointment_date__gte=current_time.date(),
            appointment_time_to__gte=current_time.time()
        )
    else:
        slotes = Add_appointment.objects.filter(
            user_booked=False,
            appointment_date__gte=current_time.date()
        ).exclude(
            appointment_date=current_time.date(),
            appointment_time_to__lt=current_time.time()
        )

    # Group slots by doctor
    doctor_slots = {}
    for slot in slotes:
        doctor = slot.doctor_id
        if doctor not in doctor_slots:
            doctor_slots[doctor] = []
        doctor_slots[doctor].append(slot)

    # Convert to a list of dictionaries for template
    slotes_list = [{'doctor': doctor, 'slots': slots} for doctor, slots in doctor_slots.items()]

    return render(request, "user/view_slotes_user.html", {"slotes": slotes_list, "selected_date": date_filter})

def payment_user(request):
    id=request.session['id']
    sid = request.GET.get('id')
    user_id=User_registration.objects.get(id=id)
    slote = Add_appointment.objects.get(id=sid)

    if request.POST:
        name=request.POST['name']
        number=request.POST['number']
        exp=request.POST['exp']
        cvv=request.POST['cvv']

        booking=Booking_slote.objects.create(
            name=name,
            number=number,
            transaction=True,
            user_booked=True,
            user_id=user_id,
            slote_id=slote,
            payment_date=timezone.now()
        )
        booking.save()
        slote.user_booked=True
        slote.save()
        messages.info(request, "Booking Confirmed")
        return redirect('/view_bookings_user')

    return render(request, "user/payment_user.html",{"slote":slote})

def view_bookings_user(request):
    id = request.session.get('id')
    if not id:
        return redirect('/login')  

    user_id = User_registration.objects.get(id=id)

    date_filter = request.GET.get('date')
    if date_filter:
        try:
            date_filter = timezone.datetime.strptime(date_filter, '%Y-%m-%d').date()
            bookings = Booking_slote.objects.filter(user_id=user_id, slote_id__appointment_date=date_filter).order_by('-slote_id__appointment_date')
        except ValueError:
            bookings = Booking_slote.objects.filter(user_id=user_id).order_by('-slote_id__appointment_date')
    else:
        bookings = Booking_slote.objects.filter(user_id=user_id).order_by('-slote_id__appointment_date')

    return render(request, "user/view_bookings_user.html", {"bookings": bookings})

def cancel_appointment_user(request):

    bid=request.GET.get('id')
    booking=Booking_slote.objects.get(id=bid)
    booking.transaction=False
    booking.user_booked=False
    booking.save()
    slote=Add_appointment.objects.get(id=booking.slote_id.id)
    slote.user_booked=False
    slote.save()
    messages.info(request,"Cancelled Successfully")

    return redirect('/view_bookings_user')

def view_doctors_user(request):

    doctors=Add_doctors.objects.all()

    return render(request,"user/view_doctors_user.html",{"doctors":doctors})

def add_complaints_user(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    doctors=Add_doctors.objects.all()

    if request.POST:
        title=request.POST['title']
        complaint=request.POST['complaint']
        doctor_id=request.POST['doctor_id']

        doctor=Add_doctors.objects.get(id=doctor_id)
        complaint=Add_complaints.objects.create(
            title=title,
            complaint=complaint,
            doctor_id=doctor,
            user_id=user_id,
            posted_date=timezone.now()
        )
        messages.info(request,"Complaint added successfull")
        complaint.save()

    return render(request,"user/add_complaints_user.html",{"doctors":doctors})

def view_complaints_user(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    complaints=Add_complaints.objects.filter(user_id=user_id)

    return render(request,"user/view_complaints_user.html",{"complaints":complaints})


def add_feedbacks_user(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    doctors=Add_doctors.objects.all()

    if request.POST:
        title=request.POST['title']
        feedback=request.POST['feedback']
        rating=request.POST['rating']
        doctor_id=request.POST['doctor_id']

        doctor=Add_doctors.objects.get(id=doctor_id)

        feedbacks=Add_feedbacks.objects.create(
            title=title,
            feedback=feedback,
            rating=rating,
            doctor_id=doctor,
            user_id=user_id,
            posted_date=timezone.now()
        )

        feedbacks.save()
        messages.info(request,"Feedback added successfull")
    return render(request,"user/add_feedbacks_user.html",{"doctors":doctors})

def view_feedbacks_user(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    feedbacks=Add_feedbacks.objects.filter(user_id=user_id)

    return render(request,"user/view_feedbacks_user.html",{"feedbacks":feedbacks})

def view_profile_user(request):

    id=request.session['id']
    users=User_registration.objects.get(id=id)

    return render(request,"user/view_profile_user.html",{"user":users})

def edit_profile_user(request):

    uid=request.GET.get('id')
    u=User_registration.objects.get(id=uid)
    if request.POST:
        name=request.POST['name']
        u.name=name
        address=request.POST['address']
        u.address=address
        contact=request.POST['contact']
        u.contact=contact
        age=request.POST['age']
        u.age=age
        profile_picture=request.FILES['profile_picture']
        u.profile_picture=profile_picture

        u.save()
        messages.info(request,"Updated Successfully")
        return redirect('/view_profile_user')

    return render(request,"user/edit_profile_user.html",{"user":u})
