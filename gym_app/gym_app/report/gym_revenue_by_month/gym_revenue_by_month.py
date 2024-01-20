# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"fieldname": "month", "label": _("Month"), "fieldtype": "Data", "width": 120},
        {"fieldname": "total_revenue", "label": _("Total Revenue"), "fieldtype": "Currency", "width": 120}
    ]

    data = get_data(filters)
    return columns, data

def get_data(filters):
    # Your logic to fetch data for the report
    # Example: Fetch total revenue for each month
    data = frappe.get_single("Gym Settings",
        filters={},
        fields=["name", "total_revenue"]
    )

    return data
