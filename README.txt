========================================================================
                      V O L U N T R A C K  -  P L A T F O R M
========================================================================
Connecting community volunteers with verified NGOs & Non-Profit Organizations.

VolunTrack is a premium web ecosystem designed to organize community-driven 
events, track volunteer participation, manage direct task assignments, and 
process secure, compliant volunteer payouts using Razorpay Payment Gateway.

------------------------------------------------------------------------
1. KEY FEATURES
------------------------------------------------------------------------
* MULTI-ROLE REGISTRATION & APPROVALS:
  - Volunteers can register, manage profiles, search events, and apply.
  - Organizers/NGOs register with Admin-approved credentials to create events.

* COMPREHENSIVE EVENT BOOKING WORKFLOW:
  - Automatic event spot counting, category classification, and scheduling.
  - Real-time work status updates (Upcoming ➔ In Process ➔ Completed ➔ Delayed).

* SECURE RAZORPAY INTEGRATION (TEST MODE):
  - Direct integration with Razorpay Checkout JS & Python SDK.
  - Secure backend cryptographic signature verification on all payments.
  - Zero-cost event auto-payout handling.

* PREMIUM TRANSACTION ANALYTICS & AUDIT LOGS:
  - High-end glassmorphic interactive dashboards for Organizer Revenue.
  - Interactive charts (Chart.js) detailing Monthly Income and Payout statuses.
  - Searchable transaction tables and audit logs for Admins & Volunteers.
  - Live PDF-printable invoice receipts containing verified transaction IDs.

* LIVE INSTANT CHAT MESSAGING:
  - Real-time communication between volunteers and organizers powered by 
    Django Channels, ASGI WebSockets, and asynchronous layers.

------------------------------------------------------------------------
2. TECH STACK & REQUIREMENTS
------------------------------------------------------------------------
* Backend Language: Python (3.10+)
* Framework: Django (6.0.2)
* Asynchronous Server: Daphne (4.2.1), Channels (4.3.2)
* Database: SQLite 3
* Payment Gateway: Razorpay (2.0.1)
* Frontend: Vanilla HTML, CSS (Bootstrap 5, custom modern palettes), JS, Chart.js

------------------------------------------------------------------------
3. DIRECTORY STRUCTURE
------------------------------------------------------------------------
volunteer_pro/
│
├── volunteer_pro/                  # Main Settings & Core Config
│   ├── settings.py                 # Settings (Auth, DB, Channels, Razorpay)
│   ├── urls.py                     # Main Routing Conf
│   ├── asgi.py                     # ASGI Configuration (Daphne/WebSockets)
│   └── wsgi.py                     # WSGI Configuration (Production)
│
├── app_modules/
│   ├── userapp/                    # Core Business & Volunteer Modules
│   │   ├── models.py               # CustomUser, booking, payment, Message
│   │   ├── views.py                # Payment, Checkout, chat views
│   │   ├── urls.py                 # Route mappings for Volunteer flows
│   │   └── forms.py                # Input forms
│   │
│   └── adminapp/                   # NGO & Administrator Modules
│       ├── models.py               # Event, Category, Attendance, Role
│       ├── views.py                # Event management and lists views
│       └── urls.py                 # Route mappings for Admin flows
│
├── templates/                      # Premium HTML layouts
│   ├── userapp/                    # Volunteer checkout, charts, invoices
│   └── adminapp/                   # Event lists, category lists, task lists
│
├── db.sqlite3                      # Database storage
├── requirements.txt                # System dependencies list
└── README.txt                      # Project information guide (This file)

------------------------------------------------------------------------
4. HOW TO RUN THE PROJECT LOCALLY
------------------------------------------------------------------------
1. Install Python 3.10+ on your system.
2. Open terminal/Command Prompt in the project root directory.
3. Install required libraries:
   pip install -r requirements.txt

4. Generate database tables and models:
   python manage.py makemigrations
   python manage.py migrate

5. Start the local Daphney/Django developmental server:
   python manage.py runserver 127.0.0.1:1235

6. Open your browser and navigate to:
   http://127.0.0.1:1235/

------------------------------------------------------------------------
5. PAYMENT TESTING CREDENTIALS (SANDBOX MODE)
------------------------------------------------------------------------
To test the checkout process, the platform is pre-loaded with Test Keys:
* Test Key ID: rzp_test_SuHJDPoOSzG2d8
* Test Key Secret: I9vELDUhWgPRScJ0TijJxHn9

Use the following official sandbox card details to simulate transactions:

* RECOMMENDED TEST CARD (DOMESTIC INDIAN VISA):
  - Card Number: 4386 2894 0766 0153
  - Expiry Date: Any future date (e.g. 12/28)
  - CVV: 111 (or any 3 digits)

* TEST CARD (DOMESTIC MASTER CARD):
  - Card Number: 5104 0155 5555 5558
  - Expiry Date: Any future date (e.g. 12/28)
  - CVV: 111 (or any 3 digits)

* TRANSACTION FLOW:
  1. Once the Razorpay popup opens, select "Cards".
  2. Input one of the test card details above.
  3. Clicking "Pay" launches a mock bank page. Click the green "Success" 
     button to verify.
  4. Entering OTP: Enter 4 or more digits (e.g. 1234) for transaction success, 
     or less than 4 digits to simulate failures.

------------------------------------------------------------------------
6. DEVELOPMENT & CONTRIBUTE
------------------------------------------------------------------------
To keep core features separated, organize additional layouts inside 
the 'templates/' directory. All code additions must comply with clean 
structural architecture, preserving backward database migrations.

&copy; 2026 VolunTrack Platform. All Rights Reserved.
========================================================================
