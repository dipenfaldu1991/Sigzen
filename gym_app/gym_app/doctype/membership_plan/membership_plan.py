# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MembershipPlan(Document):
	def on_update(self):
		frappe.enqueue("gym_app.gym_app.doctype.gym_membership_plan.calculate_revenue.execute",
                       doc=self, queue='long')
