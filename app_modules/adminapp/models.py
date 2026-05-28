from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
      
    
class Event(models.Model):
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=250)
    event_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=250) 
    required_volunteers = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250)
    event_status = models.CharField(max_length=250)
    event_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name

    @property
    def is_finished(self):
        from django.utils import timezone
        import datetime
        now = timezone.now()
        # Combine event_date and end_time to get a datetime object
        event_end = timezone.make_aware(datetime.datetime.combine(self.event_date, self.end_time))
        return now > event_end

class EventRole(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    role_name = models.CharField(max_length=250) 
    role_description = models.CharField(max_length=250)
    required_count = models.IntegerField()
    is_active = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.role_name} - {self.event.event_name}"

class VolunteerApplication(models.Model):
    volunteer = models.CharField(max_length=250)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    preferred_role = models.CharField(max_length=250)
    application_status = models.CharField(max_length=250)
    admin_remark = models.CharField(max_length=250)
    is_active = models.CharField(max_length=250)
    applied_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer} - {self.event.event_name} ({self.application_status})"
    
class TaskAssignment(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    # volunteer = models.CharField(max_length=250)
    volunter = models.ForeignKey(VolunteerApplication,on_delete=models.CASCADE)
    assigned_role = models.CharField(max_length=250)
    assigned_by = models.CharField(max_length=250)
    task_status = models.CharField(max_length=250)
    assigned_date = models.DateField()
    completed_date = models.DateField()
    remarks = models.CharField(max_length=250)
    is_active = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    

class Attendance(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    volunteer = models.CharField(max_length=250)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    total_hours =models.IntegerField()
    attendance_status = models.CharField(max_length=50)
    verified_by = models.CharField(max_length=250)
    is_active = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




