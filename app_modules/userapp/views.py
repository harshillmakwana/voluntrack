from django.shortcuts import render,redirect
import json
from django.http import HttpResponse
from app_modules.userapp import forms
from app_modules.userapp.forms import booking_form , payment_form
from app_modules.userapp.models import booking , Message, Feedback
from app_modules.adminapp import forms
from app_modules.adminapp import models
from django.contrib.auth.decorators import login_required

from app_modules.userapp.models import CustomUser
from .forms import VolunteerRegistrationForm, OrganizerRegistrationForm
from django.contrib import messages

from django.contrib.auth import login,logout

# Create your views here.
def myname(request):
    return HttpResponse("this is userapp")

# template files
@login_required(login_url='login_view')
def about_view(request):
    return render(request,'userapp/about.html')

def user_profile(request):
    return render(request,'userapp/user_profile.html')

@login_required(login_url='login_view')
def contact_view(request):
    return render(request,'userapp/contact.html')

def dashboard_view(request):
    return render(request,'userapp/dashboard.html')

@login_required(login_url='login_view')
def events_view(request):
    eve = models.Event.objects.all()   
    context = {'eve':eve}
    return render(request,'userapp/events.html',context)

def update_event(request,id):
    eve = models.Event.objects.get(id=id)
    if request.method == 'POST':
        form = forms.Event_form(request.POST,instance=eve)
        if form.is_valid():
            form.save()
            return redirect()
        else:
            print(form.errors)
    context = {'eve':eve}
    return render(request,'userapp/update_event.html',context)
    
    
 
def index_view(request):
    volunteers = CustomUser.objects.filter(role='VOLUNTEER').order_by('-created_at')[:4]
    return render(request, 'userapp/index.html', {'volunteers': volunteers})

@login_required(login_url='login_view')
def volunteers_view(request):
    
    volunteers = CustomUser.objects.filter(role='VOLUNTEER').order_by('-created_at')
    return render(request, 'userapp/volunteers.html', {'volunteers': volunteers})



def volunterr_event_show(request):
    book = booking.objects.all()
    shoow_book = booking.objects.filter(status = 'Accept')
    context = { 'book':book , 'shoow_book': shoow_book } 
    return render(request,'userapp/volunteer_booking_show.html',context)
        
# ----------------------------------------------------Authentication Views--------------------------------------------------

def volunteer_register(request):
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'VOLUNTEER'
            user.is_approved = True  
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            messages.success(request, "Registration successful! Welcome to SVMS.")
            return redirect('login_view') 
    else:
        form = VolunteerRegistrationForm()
    return render(request, 'userapp/register.html', {'form': form})

def organizer_register(request):
    if request.method == 'POST':
        passw = request.POST.get('password')
        conf_pass = request.POST.get('confirm_password')

        if passw != conf_pass:
            messages.error(request, "Passwords do not match!")
            return render(request, 'userapp/register_org.html')

        try:
            from .models import CustomUser
            user = CustomUser.objects.create_user(
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=passw,
                organization_name=request.POST.get('organization_name'),
                contact_person=request.POST.get('contact_person'),
                designation=request.POST.get('designation'),
                phone_number=request.POST.get('phone_number'),
                organization_type=request.POST.get('organization_type'),
                city=request.POST.get('city'),
                organization_description=request.POST.get('organization_description'),
                role='ORGANIZER',
                is_approved=False  
            )
            user.save()
            messages.success(request, "Registration request sent! Please wait for Admin approval.")
            return redirect('login_view')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'userapp/org_register.html')

    return render(request, 'userapp/org_register.html')

from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.role != selected_role:
                messages.error(request, f"This account is not registered as a {selected_role.lower()}.")
                return render(request, 'userapp/login.html')

            if user.role == 'ORGANIZER' and not user.is_approved:
                messages.error(request, "Your Organization account is pending Admin approval.")
                return render(request, 'userapp/login.html')

            auth_login(request, user)
            
            if user.role == 'ADMIN':
                return redirect('dashboard_view_ad')
            elif user.role == 'ORGANIZER':
                return redirect('org_dashboard')
            else:
                return redirect('index_view1')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'userapp/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login_view')

# ----------------------------------------------------Org Views--------------------------------------------------
 
 

def org_dashboard(request):
    bok_list = booking.objects.all()
    context = {'bok_list': bok_list}
    return render(request,'userapp/org_dashboard.html',context)


def org_dahs_create_category(request):
    if request.method == 'POST':
        form = forms.Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(org_dash_categoryevent)
        else:
            print(form.errors)
    return render(request,'userapp/org_dahs_create_category.html')

def org_dash_categoryevent(request):
    cat1 = models.Category.objects.all()
    context = {'cat1':cat1}
    return render(request,'userapp/org_dash_categoryevent.html',context)

def delete_org_categoryevent(request,id):
    deloegcat = models.Category.objects.get(id=id)
    deloegcat.delete()
    return redirect(org_dash_categoryevent)

def update_org_Category(request,id):
    upcat = models.Category.objects.get(id=id)
    if request.method =='POST':
        form = forms.Category_form(request.POST,instance=upcat)
        if form.is_valid():
            form.save()
            return redirect('org_dash_categoryevent')
        else:
            print(form.errors)
    context = {'upcat':upcat}
    return render(request,'userapp/update_org_Category.html',context)


def org_dash_create_event(request):
    e_cate = models.Category.objects.all()
    if request.method == 'POST':
        form = forms.Event_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(org_dash_event)
        else:
            print(form.errors)
    context = {'e_cate':e_cate}
    return render(request,'userapp/org_dash_create_event.html',context)

def org_dash_event(request):
    eve1 = models.Event.objects.all()
    context = {'eve1':eve1}
    return render(request,'userapp/org_dash_event.html',context)

def delete_org_event(request,id):
    deleve = models.Event.objects.get(id=id)
    deleve.delete()
    return redirect(org_dash_event)

def update_org_event(request,id):
    upeve = models.Event.objects.get(id=id)
    e_cate = models.Category.objects.all()
    
    if request.method == 'POST':
        form = forms.Event_form(request.POST,instance=upeve)
        if form.is_valid():
            form.save()
            return redirect(org_dash_event)
        else:
            print(form.errors)
    context = {'upeve': upeve, 'e_cate':e_cate }
    return render(request,'userapp/update_org_event.html',context)


def org_dash_create_VolunteerApplication(request):
    e_app = models.Event.objects.all()    
    if request.method == 'POST':
        form = forms.VolunteerApplication_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('org_dash_voleteer')
        else:
            print(form.errors)
    context = {'e_app': e_app}
    return render(request,'userapp/org_dash_create_VolunteerApplication.html',context )

def org_dash_voleteer(request):
    vol1 = models.VolunteerApplication.objects.all()
    context = {'vol1':vol1}
    return render(request,'userapp/org_dash_voleteer.html',context)

def delete_org_voleteer(request,id):
    delvole = models.VolunteerApplication.objects.get(id=id)
    delvole.delete()
    return redirect(org_dash_voleteer)

def update_org_VolunteerApplication(request,id):
    upvoappli = models.VolunteerApplication.objects.get(id=id)
    e_app = models.Event.objects.all()
    if request.method == 'POST':
        form = forms.VolunteerApplication_form(request.POST,instance=upvoappli)
        if form.is_valid():
            form.save()
            return redirect('org_dash_voleteer')
        else:
            print(form.errors)
    context = {'upvoappli':upvoappli,'e_app': e_app}
    return render(request,'userapp/update_org_VolunteerApplication.html',context )



# def create_booking(request):
#     e_app = models.Event.objects.all()
#     e_cat = models.Category.objects.all() 
       
#     if request.method == 'POST':
#         form = booking_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_list')
#         else:
#             print(form.errors)
#     context = {'e_app': e_app , 'e_cat': e_cat}
#     return render(request,'userapp/create_booking.html',context)



# aa view create karu tema sadu booking thay che and biju nechhe create karu te
#        j event par click kare te event nu name and category aavi jay automatic
# @login_required(login_url='login_view') 
# def create_booking(request,id): 
#     abc = models.Event.objects.get(id=id)
#     if request.method == 'POST':
#         booking.objects.create(
#             name=request.POST.get('name'),
#             email=request.POST.get('email'),
#             phone_number=request.POST.get('phone_number'),
#             categorys_id=abc.event_category,
#             event_name_id=abc,
#             booking_date=request.POST.get('booking_date'),
#             time_start=request.POST.get('time_start'),
#             time_end=request.POST.get('time_end'),
#         )
#         return redirect('booking_list')

#     return render(request,'userapp/create_booking.html',{
#         'abc': abc,
#     })


@login_required(login_url='login_view')    
def create_booking(request, id):
    abc = models.Event.objects.get(id=id)

    # Automatically create booking without filling the form
    booking.objects.create(
        name=request.user.username,
        email=request.user.email,
        phone_number=request.user.phone_number,
        categorys=abc.event_category,
        event_name=abc,
        booking_date=abc.event_date,
        time_start=abc.start_time,
        time_end=abc.end_time,
        price=abc.event_price,
    )
    return redirect('booking_list')

@login_required(login_url='login_view')
def booking_list(request):
    book_list = booking.objects.filter(email=request.user.email)
    context = {'book_list' : book_list}
    return render(request,'userapp/booking_list.html',context)

def approve_book(request, id):
    bok = booking.objects.get(id=id)
    bok.status = 'Accept'
    bok.save()
    return  redirect('org_dashboard')

def reject_book(request,id):
    bokk = booking.objects.get(id=id)
    bokk.status = 'Reject'
    bokk.save()
    return redirect(org_dashboard)

def org_booking_show(request):
    book_list = booking.objects.all()
    accept_event = booking.objects.filter(status='Accept')
    # Fetch all feedback to ensure visibility for now
    feedbacks = Feedback.objects.all().order_by('-created_at')
    context = {
        'book_list': book_list,
        'accept_event': accept_event,
        'feedbacks': feedbacks
    }
    return render(request, 'userapp/org_booking_show.html', context)

def update_process_status(request, id, status):
    bok = get_object_or_404(booking, id=id)
    bok.process_status = status
    bok.save()
    return redirect('org_booking_show')

def invoice_detail(request, id):
    from app_modules.userapp.models import payment
    bok = get_object_or_404(booking, id=id)
    pay_rec = payment.objects.filter(booking=bok, status='Paid').first()
    return render(request, 'userapp/invoice.html', {'i': bok, 'payment': pay_rec})

def submit_feedback(request, id):
    bok = get_object_or_404(booking, id=id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Feedback.objects.create(
            volunteer=request.user,
            booking=bok,
            rating=rating,
            comment=comment
        )
        return redirect('booking_list')
    return render(request, 'userapp/submit_feedback.html', {'i': bok})


def org_profille(request):
    return render(request,'userapp/org_profille.html')

def create_payment(request, id=None):
    import razorpay
    from django.conf import settings
    from django.contrib import messages
    from app_modules.userapp.models import booking, payment

    # Get the booking
    bok = get_object_or_404(booking, id=id)

    # 1. Enforce status eligibility: Booking must be 'Accept' and 'Completed'
    if bok.status != 'Accept' or bok.process_status != 'Completed':
        messages.error(request, "This booking is not eligible for payment yet. The service must be accepted and marked as Completed.")
        return redirect('org_booking_show')

    # 2. One-time payment validation (GET request): Check if already paid
    if bok.payment_status == 'Paid':
        messages.info(request, "This service/booking has already been paid successfully. You cannot pay again.")
        return redirect('invoice_detail', id=bok.id)

    # Handle free event edge case
    if bok.price <= 0:
        bok.payment_status = 'Paid'
        bok.save()
        messages.success(request, "Free booking confirmed successfully!")
        return redirect('invoice_detail', id=bok.id)

    # Initialize Razorpay Client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    if request.method == 'POST':
        # One-time payment validation (POST request): Prevents processing duplicate posts
        if bok.payment_status == 'Paid':
            messages.warning(request, "This booking has already been paid successfully.")
            return redirect('invoice_detail', id=bok.id)

        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            # Verify payment signature
            client.utility.verify_payment_signature(params_dict)
            
            # Find the pending payment record and update it
            try:
                pay_rec = payment.objects.get(razorpay_order_id=order_id)
            except payment.DoesNotExist:
                # Fallback if somehow not found, create new
                pay_rec = payment(booking=bok, razorpay_order_id=order_id)

            pay_rec.razorpay_payment_id = payment_id
            pay_rec.razorpay_signature = signature
            pay_rec.status = 'Paid'
            pay_rec.amount = bok.price
            pay_rec.save()

            # Mark booking as Paid
            bok.payment_status = 'Paid'
            bok.save()

            messages.success(request, "Payment successful! Booking confirmed.")
            return redirect('invoice_detail', id=bok.id)

        except Exception as e:
            print(f"Razorpay verification failed: {str(e)}")
            
            # Update payment record to Failed
            try:
                pay_rec = payment.objects.get(razorpay_order_id=order_id)
                pay_rec.status = 'Failed'
                pay_rec.save()
            except payment.DoesNotExist:
                pass
                
            messages.error(request, "Payment verification failed. Please try again.")
            return redirect('booking_list')

    # GET request: Create Razorpay Order
    amount_in_paise = int(bok.price * 100)
    
    order_data = {
        'amount': amount_in_paise,
        'currency': 'INR',
        'payment_capture': 1
    }

    try:
        razorpay_order = client.order.create(data=order_data)
        razorpay_order_id = razorpay_order['id']

        # Store pending payment record in DB
        payment.objects.create(
            booking=bok,
            razorpay_order_id=razorpay_order_id,
            amount=bok.price,
            status='Pending'
        )

        context = {
            'booking': bok,
            'razorpay_order_id': razorpay_order_id,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount_paise': amount_in_paise,
            'currency': 'INR'
        }
        return render(request, 'userapp/create_payment.html', context)

    except Exception as e:
        print(f"Error creating Razorpay order: {str(e)}")
        messages.error(request, "Could not initialize payment gateway. Please try again later.")
        return redirect('org_booking_show')


    
    
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Message

User = get_user_model()

# ======================
# UNIFIED CHAT PAGE
# ======================
@login_required
def chat_index(request):
    # Get users the current user has chatted with
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-created')
    
    contact_ids = set()
    for m in messages:
        if m.sender != request.user:
            contact_ids.add(m.sender.id)
        if m.receiver != request.user:
            contact_ids.add(m.receiver.id)
            
    # Add an active user to contacts if explicitly requested via query param
    chat_with = request.GET.get('user')
    user_email = request.GET.get('email')
    org_name = request.GET.get('org_name')
    
    if chat_with and chat_with.isdigit():
        contact_ids.add(int(chat_with))
    elif user_email:
        target_user = User.objects.filter(email=user_email).first()
        if target_user:
            contact_ids.add(target_user.id)
            chat_with = str(target_user.id)
    elif org_name:
        # Try to find organizer by organization_name, or even username if it matches
        target_user = User.objects.filter(Q(organization_name__icontains=org_name) | Q(username__icontains=org_name), role='ORGANIZER').first()
        if target_user:
            contact_ids.add(target_user.id)
            chat_with = str(target_user.id)
            
    # Get all potential contacts based on role
    if request.user.role == 'VOLUNTEER':
        # Volunteers see all Organizers
        potential_contacts = User.objects.filter(role='ORGANIZER')
    elif request.user.role == 'ORGANIZER':
        # Organizers see all Volunteers
        potential_contacts = User.objects.filter(role='VOLUNTEER')
    else:
        # Fallback for admin or others
        potential_contacts = User.objects.filter(id__in=contact_ids)

    # Convert to list to ensure we can annotate with unread_count reliably
    contacts_list = list(potential_contacts)

    # Add unread counts to each contact
    for contact in contacts_list:
        contact.unread_count = Message.objects.filter(
            sender=contact, 
            receiver=request.user, 
            is_read=False
        ).count()

    return render(request, "userapp/chat.html", {
        "contacts": contacts_list,
        "active_chat_id": chat_with
    })


# ======================
# OPEN CHAT ROOM (Fallback/Direct access)
# ======================
@login_required
def chat_room(request, id):
    other = get_object_or_404(User, id=id)

    # Mark messages as read
    Message.objects.filter(sender=other, receiver=request.user, is_read=False).update(is_read=True)

    msgs = Message.objects.filter(
        Q(sender=request.user, receiver=other) |
        Q(sender=other, receiver=request.user)
    ).order_by("created")

    return render(request, "userapp/chat.html", {
        "other": other,
        "msgs": msgs
    })


# ======================
# GET OLD MESSAGES AJAX
# ======================
@login_required
def get_messages(request, id):
    other = get_object_or_404(User, id=id)

    # Mark messages as read
    Message.objects.filter(sender=other, receiver=request.user, is_read=False).update(is_read=True)

    messages = Message.objects.filter(
        sender__in=[request.user, other],
        receiver__in=[request.user, other]
    ).order_by("created")

    data = []
    for m in messages:
        data.append({
            "id": m.id,
            "sender": m.sender.username,
            "message": m.text,
            "time": str(m.created.strftime("%H:%M"))
        })

    return JsonResponse({
        "messages": data,
        "other_username": other.username
    })

# ======================
# SEND MESSAGE AJAX
# ======================
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def send_message(request, id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            msg_text = data.get("message")
            if not msg_text:
                return JsonResponse({"status": "error", "message": "No message text provided"})
                
            other = get_object_or_404(User, id=id)
            msg = Message.objects.create(
                sender=request.user,
                receiver=other,
                text=msg_text
            )
            print(f"Message stored: {msg.id} from {request.user.username} to {other.username}")
            return JsonResponse({"status": "success", "id": msg.id})
        except Exception as e:
            print(f"Error in send_message: {str(e)}")
            return JsonResponse({"status": "error", "message": str(e)})
            
    return JsonResponse({"status": "error", "message": "Invalid request method"})


# ======================
# DELETE SINGLE MESSAGE
# ======================
@login_required
def delete_message(request, id):
    msg = get_object_or_404(Message, id=id, sender=request.user)
    msg.delete()
    return JsonResponse({"status": "deleted"})


# ======================
# CLEAR FULL CHAT
# ======================
@login_required
def clear_chat(request, id):
    Message.objects.filter(
        Q(sender=request.user, receiver_id=id) |
        Q(sender_id=id, receiver=request.user)
    ).delete()

    return JsonResponse({"status": "cleared"})


@login_required
def payment_history(request):
    import json
    from collections import defaultdict
    from app_modules.userapp.models import booking, payment
    from django.db.models import Sum

    # 1. Fetch successful payments
    paid_payments = payment.objects.filter(status='Paid').order_by('-created_at')
    
    # 2. Aggregates
    total_revenue = sum(p.amount for p in paid_payments)
    total_transactions = payment.objects.count()
    paid_count = paid_payments.count()
    pending_count = payment.objects.filter(status='Pending').count()
    failed_count = payment.objects.filter(status='Failed').count()

    # 3. Pending inflow (Accepted bookings with pending payment)
    pending_bookings = booking.objects.filter(status='Accept', payment_status='Pending')
    pending_revenue = sum(b.price for b in pending_bookings)

    # 4. Monthly Revenue grouping
    monthly_map = defaultdict(float)
    # Order chronologically for the chart
    for p in reversed(paid_payments):
        if p.created_at:
            month_key = p.created_at.strftime('%b %Y')
            monthly_map[month_key] += float(p.amount)
            
    monthly_labels = list(monthly_map.keys())
    monthly_values = list(monthly_map.values())

    # 5. Fetch all payment list for the audit table
    all_payments = payment.objects.all().order_by('-created_at')

    context = {
        'total_revenue': total_revenue,
        'pending_revenue': pending_revenue,
        'total_transactions': total_transactions,
        'paid_count': paid_count,
        'pending_count': pending_count,
        'failed_count': failed_count,
        'monthly_labels_json': json.dumps(monthly_labels),
        'monthly_values_json': json.dumps(monthly_values),
        'payments': all_payments
    }
    return render(request, 'userapp/payment_history.html', context)
