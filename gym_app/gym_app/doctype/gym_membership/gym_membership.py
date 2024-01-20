# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class GymMembership(Document):
	def on_update(self):
		frappe.enqueue("gym_app.gym_app.doctype.gym_membership.calculate_revenue.execute",
                       doc=self, queue='long')
	def validate(self):
		existing_membership = frappe.db.exists({
            "doctype": "Gym Membership",
            "member": self.member
        })
		print("=========================",existing_membership)
		if existing_membership:
			member = frappe.get_doc("Gym Member", self.member)
			frappe.throw(_("Gym Membership with email {0} already exists.").format(member.email))
		else:
			membership_type = frappe.get_doc("Membership Plan", self.membership_type)
			self.amount = membership_type.price