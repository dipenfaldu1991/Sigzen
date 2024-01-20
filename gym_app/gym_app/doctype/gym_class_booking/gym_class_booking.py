# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now_datetime, get_first_day, get_last_day, add_days

class GymClassBooking(Document):
    def validate(self):
        # Check if the class is full
        booked_slots = frappe.get_all(
            'Gym Class Booking',
            filters={'class_type': self.class_type, 'booking_date': self.booking_date, 'attendance_status': 'Present', 'docstatus': 0},
            as_list=True
        )
        total_slots = frappe.get_value('Gym Class', {'class_type':self.class_type}, 'total_slots')
        if len(booked_slots) >= total_slots:
            frappe.throw(_('Sorry, the class is already full. Please choose another class.'))

    def on_submit(self):
        # Send confirmation email to the customer
        print("===============================================================")
        send_booking_confirmation_email(self.member, self.class_type, self.booking_date)

def send_booking_confirmation_email(member, class_type, booking_date):
    # Placeholder function to send confirmation email
    # This function should send an email to the customer confirming the class booking
    # You can use the frappe.sendmail function or any other method to send emails
    # Fetch member's email from the Gym Member doctype
    member_email = frappe.get_value('Gym Member', member, 'email')
    print(member_email)
    # Create the email subject and message
    subject = _('Booking Confirmation for {0} on {1}').format(class_type, booking_date)
    message = _('Thank you for booking {0} on {1}. We look forward to seeing you in the class!').format(class_type, booking_date)

    try:
        # Send the email
        frappe.sendmail(
            recipients=member_email,
            subject=subject,
            message=message,
            content_type='text/html'
        )
        print('test')
        frappe.msgprint(_('Booking confirmation email sent successfully.'))
    except Exception as e:
        frappe.log_error(_('Failed to send booking confirmation email: {0}').format(str(e)))

    return True
    pass



@frappe.whitelist()
def send_weekly_summary():
    start_date = get_first_day(add_days(now_datetime(), -7))
    end_date = get_last_day(add_days(now_datetime(), -1))

    bookings = frappe.get_all(
        'Gym Class Booking',
        filters={'booking_date': ['between', (start_date, end_date)], 'docstatus': 0},
        fields=['member', 'class_type', 'booking_date', 'attendance_status']
    )

    member_bookings = {}
    for booking in bookings:
        member = booking.member
        if member not in member_bookings:
            member_bookings[member] = []
        member_bookings[member].append({
            'class_type': booking.class_type,
            'booking_date': booking.booking_date,
            'attendance_status': booking.attendance_status
        })

    for member, bookings in member_bookings.items():
        send_weekly_summary_email(member, bookings)

def send_weekly_summary_email(member, bookings):
    # Construct the email subject and message
    subject = _('Weekly Class Booking Summary')
    message = f"Dear {member},\n\nHere is your weekly class booking summary:\n\n"
    
    for booking in bookings:
        message += f"Class Type: {booking['class_type']}\n"
        message += f"Booking Date: {booking['booking_date']}\n"
        message += f"Attendance Status: {booking['attendance_status']}\n\n"

    # Placeholder email sending logic
    # You should replace the following line with the actual code to send the email
    # frappe.msgprint(f"Email sent to {member} with weekly class booking summary.")

    frappe.sendmail(recipients=member, subject=subject, message=message, content_type='text/plain')