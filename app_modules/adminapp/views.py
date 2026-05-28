from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from app_modules.adminapp import forms
from app_modules.adminapp import models

# Create your views here.
def myname(request):
    return HttpResponse("this is adminapp")

# template files


def apply_event_view(request):
    return render(request,'adminapp/apply_event.html')

def attendance_history_view(request):
    return render(request,'adminapp/attendance_history.html')

def certificates_view(request):
    return render(request,'adminapp/certificates.html')

def checkin_view(request):
    return render(request,'adminapp/checkin.html')

def checkout_view(request):
    return render(request,'adminapp/checkout.html')



def dashboard_view_ad(request):
    # Badha users fetch karo
    all_users = CustomUser.objects.all().order_by('-created_at')
    
    # Baki na stats (je pela cards mate banaya hata)
    total_users = all_users.exclude(role='ADMIN').count()
    approved_count = all_users.filter(role='ORGANIZER', is_approved=True).count()
    pending_count = all_users.filter(role='ORGANIZER', is_approved=False).count()

    context = {
        'all_users': all_users,
        'total_users': total_users,
        'approved_count': approved_count,
        'pending_count': pending_count,
    }
    return render(request, 'adminapp/dashboard.html', context)

from django.contrib import messages

def update_status(request, user_id, action):
    # User object fetch karo
    user_item = get_object_or_404(CustomUser, id=user_id)
    
    # Only Organizer mate j status update thavu joie
    if user_item.role == 'ORGANIZER':
        if action == 'approve':
            user_item.is_approved = True
            messages.success(request, f"Organization '{user_item.organization_name}' is now Approved!")
        elif action == 'reject':
            user_item.is_approved = False
            messages.warning(request, f"Organization '{user_item.organization_name}' has been Rejected.")
        
        user_item.save()
    else:
        messages.error(request, "Status can only be updated for Organizations.")

    # Pachhu dashboard par redirect
    return redirect('dashboard_view')
    
def event_detail_view(request):
    return render(request,'adminapp/event_detail.html')

def event_list_view(request):
    return render(request,'adminapp/event_list.html')

def forgot_password_view(request):
    return render(request,'adminapp/forgot_password.html')

def login_view(request):
    return render(request,'adminapp/login.html')

def my_applications_view(request):
    return render(request,'adminapp/my_applications.html')

def my_tasks_view(request):
    return render(request,'adminapp/my_tasks.html')

def profile_edit_view(request):
    return render(request,'adminapp/profile_edit.html')

def profile_view_view(request):
    return render(request,'adminapp/profile_view.html')

def register_view(request):
    return render(request,'adminapp/register.html')

def reset_password_view(request):
    return render(request,'adminapp/reset_password.html')

def admin_profile(request):
    return render(request,'adminapp/admin_profile.html')

from app_modules.userapp.models import CustomUser

def all_users(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request,'adminapp/all_users.html',context)


def create_Event(request):
    e_cate = models.Category.objects.all()
    context = {'e_cate':e_cate}
    if request.method == 'POST':
        form = forms.Event_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_Event')
        else:
            print(form.errors)
    return render(request,'adminapp/create_Event.html',context) 

def list_Event(request):
    event = models.Event.objects.all()
    context = {'event': event }
    return render(request,'adminapp/list_Event.html',context)

def delete_event(request,id):
    deleve = models.Event.objects.get(id=id)
    deleve.delete()
    return redirect(list_Event)

def update_event(request,id):
    upeve = models.Event.objects.get(id=id)
    e_cate = models.Category.objects.all()
    
    if request.method == 'POST':
        form = forms.Event_form(request.POST,instance=upeve)
        if form.is_valid():
            form.save()
            return redirect(list_Event)
        else:
            print(form.errors)
    context = {'upeve': upeve, 'e_cate':e_cate }
    return render(request,'adminapp/update_event.html',context)




def create_EventRole(request):
    e_role  = models.Event.objects.all()
    if request.method == 'POST':
        form = forms.EventRole_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_EventRole')
        else:
            print(form.errors)
    context = {'e_role':e_role}
    return render(request,'adminapp/create_EventRole.html',context)

def list_EventRole(request):
    erole = models.EventRole.objects.all()
    context = {'erole': erole, }
    return render(request,'adminapp/list_EventRole.html',context)

def detete_role(request,id):
    delrole = models.EventRole.objects.get(id=id)
    delrole.delete()
    return redirect('list_EventRole')

def update_EventRole(request,id):
    e_role  = models.Event.objects.all()
    uprole = models.EventRole.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EventRole_form(request.POST,instance=uprole)
        if form.is_valid():
            form.save()
            return redirect('list_EventRole')
        else:
            print(form.errors)
    context = {'uprole':uprole ,'e_role':e_role}
    return render(request,'adminapp/update_EventRole.html',context)


def create_VolunteerApplication(request):
    e_app = models.Event.objects.all()
    context = {'e_app': e_app}
    if request.method == 'POST':
        form = forms.VolunteerApplication_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_VolunteerApplication')
        else:
            print(form.errors)
    return render(request,'adminapp/create_VolunteerApplication.html',context )

def list_VolunteerApplication(request):
    voapp = models.VolunteerApplication.objects.all()
    context = {'voapp': voapp }
    return render(request,'adminapp/list_VolunteerApplication.html',context)

def delete_volappli(request,id):
    delvoapp = models.VolunteerApplication.objects.get(id=id)
    delvoapp.delete()
    return redirect(list_VolunteerApplication) 

def update_VolunteerApplication(request,id):   
    upvoappli = models.VolunteerApplication.objects.get(id=id)
    e_app = models.Event.objects.all()
    if request.method == 'POST':
        form = forms.VolunteerApplication_form(request.POST,instance=upvoappli)
        if form.is_valid():
            form.save()
            return redirect('list_VolunteerApplication')
        else:
            print(form.errors)
    context = {'upvoappli':upvoappli,'e_app': e_app}
    return render(request,'adminapp/update_VolunteerApplication.html',context )



def create_TaskAssignment(request):    
    e_task = models.Event.objects.all()
    voli = models.VolunteerApplication.objects.all()
    context = {'e_task': e_task, 'voli' : voli}
    if request.method == 'POST':
        form = forms.TaskAssignment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_TaskAssignment')
        else:
            print(form.errors)
    return render(request,'adminapp/create_TaskAssignment.html',context)

def list_TaskAssignment(request):
    task = models.TaskAssignment.objects.all()
    context = {'task': task }
    return render(request,'adminapp/list_TaskAssignment.html',context)

def delete_taskassi(request,id):
    deltskassi = models.TaskAssignment.objects.get(id=id)
    deltskassi.delete()
    return redirect(list_TaskAssignment)

def update_TaskAssignment(request,id):
    uptaskass = models.TaskAssignment.objects.get(id=id)    
    e_task = models.Event.objects.all()
    if request.method == 'POST':
        form = forms.TaskAssignment_form(request.POST,instance=uptaskass)
        if form.is_valid():
            form.save()
            return redirect('list_TaskAssignment')
        else:
            print(form.errors)
    context = {'uptaskass': uptaskass ,'e_task': e_task }
    return render(request,'adminapp/update_TaskAssignment.html',context)



def create_Attendance(request):
    e_atte = models.Event.objects.all()
    context = {'e_atte': e_atte}
    if request.method == 'POST':
        form = forms.Attendance_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_Attendance')
        else:
            print(form.errors)
    return render(request,'adminapp/create_Attendance.html',context)

def list_Attendance(request):
    attends = models.Attendance.objects.all()
    context = {'attends' : attends}
    return render(request,'adminapp/list_Attendance.html',context)

def delete_attedance(request,id):
    delatte = models.Attendance.objects.get(id=id)
    delatte.delete()
    return redirect(list_Attendance)

def update_Attendance(request,id):
    upatte = models.Attendance.objects.get(id=id)
    e_atte = models.Event.objects.all()
    context = {'e_atte': e_atte}
    if request.method == 'POST':
        form = forms.Attendance_form(request.POST,instance=upatte)
        if form.is_valid():
            form.save()
            return redirect('list_Attendance')
        else:
            print(form.errors)
    context = {'upatte': upatte,'e_atte': e_atte}
    return render(request,'adminapp/update_Attendance.html',context)


def create_Category(request):
    if request.method =='POST':
        form = forms.Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_Category')
        else:
            print(form.errors)
    return render(request,'adminapp/create_Category.html')

def list_Category(request):
    cate = models.Category.objects.all()
    context = {'cate':cate}
    return render(request,'adminapp/list_Category.html',context)

def delete_category(request,id):
    delcate = models.Category.objects.get(id=id)
    delcate.delete()
    return redirect(list_Category)

def update_Category(request,id):
    upcat = models.Category.objects.get(id=id)
    if request.method =='POST':
        form = forms.Category_form(request.POST,instance=upcat)
        if form.is_valid():
            form.save()
            return redirect('list_Category')
        else:
            print(form.errors)
    context = {'upcat':upcat}
    return render(request,'adminapp/update_Category.html',context)


def list_payments(request):
    from app_modules.userapp.models import payment
    from django.core.paginator import Paginator
    payments_list = payment.objects.all().order_by('-created_at')
    paginator = Paginator(payments_list, 10)  # Show 10 payments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'payments': page_obj}
    return render(request, 'adminapp/list_payments.html', context)