# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe

from frappe.utils import nowdate
from frappe import _

def get_fitness_data(member_name):
    # Fetch fitness data for the given member
    fitness_data = frappe.get_all(
        "Fitness Record",
        filters={"member": member_name},
        fields=["date", "weight_kg", "calories_burned"],

    )

    return fitness_data

def execute(filters=None):

    columns = [
        {"label": _("Customer"), "fieldname": "member", "fieldtype": "Link", "options": "Gym Member", "width": 120},
        {"label": _("Date"), "fieldname": "date", "fieldtype": "Date", "width": 100},
        {"label": _("Weight"), "fieldname": "weight_kg", "fieldtype": "Float", "width": 80},
        {"label": _("Calories"), "fieldname": "calories_burned", "fieldtype": "Float", "width": 80},
        # Add other fields as needed
    ]

    data = []

    # Fetch data from Gym Member and Gym Membership
    members = frappe.get_all("Gym Member", filters={}, fields=["name", "first_name", "last_name"])
    for member in members:
        gym_membership = frappe.get_all("Gym Membership", filters={"member": member.name}, fields=["start_date", "end_date", "amount", "payment_status"])

        # Fetch fitness data (replace this with actual data fetching logic)
        fitness_data = get_fitness_data(member.name)

        for entry in fitness_data:
            row = {
                "customer": member.first_name,
                "date": entry.get("date"),
                "weight_kg": entry.get("weight_kg"),
                "calories_burned": entry.get("calories_burned"),
                # Add other fields as needed
            }
            data.append(row)
    chart = {
        "data": {
            "labels": ["Date 1", "Date 2", "Date 3"],  # Replace with actual date labels
            "datasets": [
                {
                    "name": _("weight_kg"),
                    "values": [70, 72, 68],  # Replace with actual weight data
                },
                {
                    "name": _("calories_burned"),
                    "values": [2000, 1800, 2200],  # Replace with actual calories data
                },
            ],
        },
        "type": "line",  # You can choose other chart types like "bar", "pie", etc.
    }
    return columns, data, None, chart
