# Copyright (c) 2024, Dipen and Contributors
# See license.txt

import frappe
import unittest

class TestGymTrainer(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")  # Set a test user
        frappe.db.sql("DELETE FROM `tabGymTrainer`")  # Clear existing records
        frappe.db.commit()

    def test_valid_doctor_creation(self):
        # Test case for creating a trainer with valid data
        trainer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_number": "1234567890",
            "email": "john.doe@example.com",
            "specialization": "Cardiologist",
            "average_rating": 4.5,
        }

        trainer = frappe.get_doc({"doctype": "Gym Trainer", **trainer_data})
        trainer.insert()

        self.assertIsNotNone(trainer.name)

    def test_missing_required_fields(self):
        # Test case for creating a trainer with missing required fields
        trainer_data = {
            "last_name": "Doe",
            "contact_number": "1234567890",
            "email": "john.doe@example.com",
        }

        trainer = frappe.get_doc({"doctype": "Gym Trainer", **trainer_data})

        with self.assertRaises(frappe.ValidationError):
            trainer.insert()

    def test_invalid_contact_number(self):
        # Test case for creating a trainer with an invalid contact number
        trainer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_number": "invalid_number",  # Invalid contact number
            "email": "john.doe@example.com",
            "specialization": "Cardiologist",
            "average_rating": 4.5,
        }

        trainer = frappe.get_doc({"doctype": "Gym Trainer", **trainer_data})

        with self.assertRaises(frappe.ValidationError):
            trainer.insert()

    def test_invalid_email(self):
        # Test case for creating a trainer with an invalid email
        trainer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_number": "1234567890",
            "email": "invalid_email",  # Invalid email
            "specialization": "Cardiologist",
            "average_rating": 4.5,
        }

        trainer = frappe.get_doc({"doctype": "Gym Trainer", **trainer_data})

        with self.assertRaises(frappe.ValidationError):
            trainer.insert()


if __name__ == '__main__':
    unittest.main()