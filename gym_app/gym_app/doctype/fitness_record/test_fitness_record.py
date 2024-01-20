# Copyright (c) 2024, Dipen and Contributors
# See license.txt

import frappe
import unittest
from frappe.utils import now

class TestFitnessRecord(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")  # Set a test user
        frappe.db.sql("DELETE FROM `tabFitness Record`")  # Clear existing records
        frappe.db.sql("DELETE FROM `tabGym Member`")  # Clear existing gym members
        frappe.db.sql("DELETE FROM `tabGym Workout Plan Exercise`")  # Clear existing exercises
        frappe.db.commit()

        # Create a test gym member
        self.gym_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "John",
            "last_name": "Doe",
        })
        self.gym_member.insert()

        # Create a test exercise type
        self.exercise_type = frappe.get_doc({
            "doctype": "Gym Workout Plan Exercise",
            "exercise_name": "Running",
        })
        self.exercise_type.insert()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def test_valid_fitness_record_creation(self):
        # Test case for creating a fitness record with valid data
        fitness_record_data = {
            "member": self.gym_member.name,
            "date": now(),
            "weight_kg": 70.5,
            "calories_burned": 500,
            "exercise_type": self.exercise_type.name,
        }

        fitness_record = frappe.get_doc({"doctype": "Fitness Record", **fitness_record_data})
        fitness_record.insert()

        self.assertIsNotNone(fitness_record.name)

    def test_missing_required_fields(self):
        # Test case for creating a fitness record with missing required fields
        fitness_record_data = {
            "member": self.gym_member.name,
            "exercise_type": self.exercise_type.name,
        }

        fitness_record = frappe.get_doc({"doctype": "Fitness Record", **fitness_record_data})

        with self.assertRaises(frappe.ValidationError):
            fitness_record.insert()

    def test_valid_measurement_date(self):
        # Test case for setting a valid measurement date
        fitness_record_data = {
            "member": self.gym_member.name,
            "date": now(),
            "measurement_date": now(),
        }

        fitness_record = frappe.get_doc({"doctype": "Fitness Record", **fitness_record_data})
        fitness_record.insert()

        self.assertIsNotNone(fitness_record.measurement_date)


if __name__ == '__main__':
    unittest.main()
