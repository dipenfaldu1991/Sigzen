# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymTrainer(Document):
	def after_insert(self):
		self.create_user_from_gym_trainer()
		
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
            "user_type": "Gym Trainer"
        }).insert(ignore_permissions=True)

        # Link Gym existing_user to User
		self.user = new_user.name

        # Assign roles to the user (customize as needed)
		new_user.add_roles("Gym Trainer")

        # Save the changes to the Gym Member
		self.save(ignore_permissions=True)

	def validate(self):
		frappe.enqueue("gym_app.gym_app.doctype.gym_trainer.calculate_average_rating.calculate_average_rating",
                       doc=self,queue='long')
	