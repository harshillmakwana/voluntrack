import os
import sys
import django

# Set up django environment
sys.path.append(r'd:\Project\volunteer_project\volunteer_pro')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volunteer_pro.settings')
django.setup()

from app_modules.userapp.models import booking, payment

print("--- RECENT BOOKINGS ---")
bookings = booking.objects.all().order_by('-id')[:5]
for b in bookings:
    print(f"ID: {b.id}, Name: {b.name}, Price: {b.price}, Status: {b.status}, Payment Status: {b.payment_status}")

print("\n--- RECENT PAYMENTS ---")
payments = payment.objects.all().order_by('-id')[:5]
for p in payments:
    print(f"ID: {p.id}, Booking ID: {p.booking_id if p.booking else 'None'}, Order ID: {p.razorpay_order_id}, Payment ID: {p.razorpay_payment_id}, Status: {p.status}, Created: {p.created_at}")
