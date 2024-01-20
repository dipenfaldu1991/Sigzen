import frappe
from frappe import _

def execute(doc, method):
    payment_date = doc.payment_date

    if payment_date:
        # Extract the month and year from the payment date
        month, year = frappe.utils.getdate(payment_date).strftime('%m'), frappe.utils.getdate(payment_date).strftime('%Y')

        # Fetch all the memberships with the payment date within the given month
        memberships = frappe.get_all("Gym Membership",
            filters={"payment_date": [">=", f"{year}-{month}-01"], "payment_date": ["<", f"{year}-{month + 1}-01"]},
            fields=["name", "amount"]
        )

        total_revenue = sum([membership.get("amount") for membership in memberships])

        # Update the total revenue in the Gym Settings (assuming there is only one Gym Settings document)
        gym_settings = frappe.get_single("Gym Settings")
        gym_settings.db_set("total_revenue", total_revenue)