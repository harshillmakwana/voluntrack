from django.db import models
from django.contrib.auth.models import AbstractUser
from app_modules.adminapp.models import Category,Event

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('ORGANIZER', 'Organizer'),
        ('VOLUNTEER', 'Volunteer'),
    )

    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )

    AVAILABILITY_CHOICES = (
        ('FULL_TIME', 'Full Time'),
        ('WEEKENDS', 'Weekends Only'),
        ('WEEKDAYS', 'Weekdays Only'),
        ('EVENINGS', 'Evenings Only'),
        ('FLEXIBLE', 'Flexible'),
    )
   
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='VOLUNTEER')
    is_approved = models.BooleanField(default=False)

    city = models.CharField(max_length=100, null=True, blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)

    organization_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=150, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    organization_type = models.CharField(max_length=100, null=True, blank=True)
    organization_description = models.TextField(null=True, blank=True)

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 🔹 Username Config
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  
    def __str__(self):
        return f"{self.email} ({self.role})"
    
class booking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    categorys = models.ForeignKey(Category,on_delete=models.CASCADE)
    event_name = models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    
    STATUS_CHOICES = (
        ('panding', 'panding'),
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='panding')

    PROCESS_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('In Process', 'In Process'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed'),
    )
    process_status = models.CharField(max_length=20, choices=PROCESS_CHOICES, default='Upcoming')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    
class payment(models.Model):
    booking = models.ForeignKey(booking, on_delete=models.CASCADE, null=True, blank=True)
    razorpay_order_id = models.CharField(max_length=150, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=150, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=250, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, default='Pending')
    pay_type = models.CharField(max_length=50, default='Razorpay')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Payment {self.razorpay_order_id} - {self.status}"
    
    
from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )

    text = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    volunteer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_feedback')
    booking = models.OneToOneField(booking, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.booking.event_name.event_name} by {self.volunteer.username}"

  
            