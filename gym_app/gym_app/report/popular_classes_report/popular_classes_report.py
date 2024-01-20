# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe


from frappe import _

def execute(filters=None):
    columns = [
        {"fieldname": "class_type", "label": _("Class Type"), "fieldtype": "Link", "options": "Gym Class", "width": 120},
        {"fieldname": "booking_count", "label": _("Booking Count"), "fieldtype": "Int", "width": 120}
    ]

    data = get_data(filters)
    return columns, data

def get_data(filters):
    # Your logic to fetch data for the report
    # Example: Fetch class types and their booking counts
    data = frappe.db.sql("""
        SELECT `class_type`, COUNT(`name`) as `booking_count`
        FROM `tabGym Class Booking`
        WHERE `attendance_status` = 'Present'
        GROUP BY `class_type`
        ORDER BY `booking_count` DESC
    """, as_dict=True)

    return data
