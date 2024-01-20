# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class GymMember(Document):
    def after_insert(self):
        self.create_user_from_gym_member()

    # def add_gym_member_role(self):
    #     frappe.get_doc({
    #         "doctype": "UserRole",
    #         "role": "Gym Member",
    #         "parent": self.name,
    #         "parentfield": "user_roles",
    #         "parenttype": self.doctype
    #     }).insert(ignore_permissions=True)

    # def validate(self):
    #     self.create_user_from_gym_member()

    def create_user_from_gym_member(self):
        # Check if the user with the given email already exists
        existing_user = frappe.get_all("User", filters={"email": self.email}, fields=["name"])
        
        if len(existing_user) > 0:
            frappe.msgprint(_("User already exists with this email."))
            return

        # Create a new User
        new_user = frappe.get_doc({
            "doctype": "User",
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": frappe.scrub(self.email),
            "new_password": frappe.generate_hash("password123"),  # Set a secure password
            "enabled": 1,  # Enable the user
            "send_welcome_email": 1,  # Set to 1 if you want to send a welcome email
            "user_type": "Gym Member"
        }).insert(ignore_permissions=True)

        # Link Gym Member to User
        self.user = new_user.name

        # Assign roles to the user (customize as needed)
        new_user.add_roles("Gym Member")

        # Save the changes to the Gym Member
        self.save(ignore_permissions=True)

@frappe.whitelist()
def check_record_exists(doctype, filters):
    result = frappe.get_list(doctype, filters=filters, limit=1)
    return True if result else False