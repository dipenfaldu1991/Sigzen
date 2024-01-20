# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class GymLockerBooking(Document):
    def validate(self):
        self.validate_locker_availability()

    def validate_locker_availability(self):
        # Check if the selected locker is already booked
        existing_booking = frappe.db.exists({
            "doctype": "Gym Locker Booking",
            "locker_number": self.locker_number,
            "status": "Booked",
            "name": ("!=", self.name) if self.name else None  # Exclude the current document during update
        })

        if existing_booking:
            frappe.throw(f"Locker {self.locker_number} is already booked on {self.booking_date}")

@frappe.whitelist()
def validate_locker_booking(doctype, filters):
    max_lockers = frappe.get_single('Gym Settings').max_lockers
    # Check if the number of existing locker bookings exceeds the maximum
    booked_lockers = frappe.get_list(doctype, filters=filters, limit=1)
    if booked_lockers:
        return 'This Locker number is booked.'
    booked_lockers_count = frappe.db.count(doctype, {'status': 'Booked'})
    if booked_lockers_count >= max_lockers:
        return 'Maximum number of lockers booked. Cannot book more lockers.'
        



def validate(doc, method):
    validate_locker_count_per_bench(doc)

def validate_locker_count_per_bench(doc):
    # Define the maximum allowed locker bookings per bench
    max_locker_bookings_per_bench = 5  # Adjust this value as needed

    # Get the count of locker bookings for the selected bench, date, and time
    existing_bookings = frappe.get_all(
        'Gym Locker Booking',
        filters={
            'bench': doc.bench,
            'booking_date': doc.booking_date,
            'booking_time': doc.booking_time,
            'name': ['!=', doc.name] if doc.name else None  # Exclude the current booking if updating
        },
        fields=['name']
    )

    # Check if the count exceeds the limit
    if len(existing_bookings) >= max_locker_bookings_per_bench:
        frappe.throw(_("Locker booking limit reached for the selected bench, date, and time."))