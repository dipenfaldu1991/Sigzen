# Copyright (c) 2024, Dipen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FitnessRecord(Document):
    def validate(self):
        self.validate_measurement_date()
        self.calculate_bmi()

    def validate_measurement_date(self):
        # Ensure that the measurement date is not in the future
        if self.measurement_date and self.measurement_date > frappe.utils.nowdate():
            frappe.throw("Measurement Date cannot be in the future")

    def calculate_bmi(self):
        # Calculate BMI based on weight and height if available
        if self.weight_kg and self.docstatus == 0:  # Only calculate BMI for draft documents
            gym_member = frappe.get_doc("Gym Member", self.member)
            if gym_member.height:
                height_in_meters = gym_member.height / 100
                self.bmi = round(self.weight_kg / (height_in_meters ** 2), 2)

    def on_submit(self):
        self.update_member_fitness_status()

    def update_member_fitness_status(self):
        # Implement logic to update member's fitness status based on metrics
        # For example, set a flag if BMI is within a healthy range
        if self.bmi and 18.5 <= self.bmi <= 24.9:
            gym_member = frappe.get_doc("Gym Member", self.member)
            gym_member.fitness_status = "Healthy"
            gym_member.save()

    def on_cancel(self):
        self.reset_member_fitness_status()

    def reset_member_fitness_status(self):
        # Reset member's fitness status when Gym Metrics record is cancelled
        gym_member = frappe.get_doc("Gym Member", self.member)
        gym_member.fitness_status = None
        gym_member.save()
