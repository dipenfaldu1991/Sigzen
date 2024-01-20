# Copyright (c) 2024, Dipen and Contributors
# See license.txt

# Import Frappe Test Library
import frappe
import unittest

# Extend FrappeTestCase to use Frappe's testing features
class TestGymMember(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")  # Set a test user
        frappe.db.sql("DELETE FROM `tabGym Member`")  # Clear existing records
        frappe.db.commit()
        # Create a Gym Member
        self.gym_member = frappe.get_doc({
            'doctype': 'Gym Member',
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'gender': 'Male',
            'contact_number': '1234567890',
            'email': 'john.doe@example.com',
            'address': '123 Main Street, City',
            'emergency_contact_details': 'Emergency Contact Name: Jane, Phone: 9876543210',
            'joining_date': '2024-01-01',
            'height': 180.0,
            'weight': 75.0,
            'registration_date': '2024-01-01',
            # Add other necessary fields
        })
        self.gym_member.insert()

    def tearDown(self):
        # Delete the Gym Member created during setup
        frappe.delete_doc('Gym Member', self.gym_member.name)

    def test_create_gym_member(self):
        # Fetch the Gym Member to ensure it was saved
        saved_gym_member = frappe.get_doc('Gym Member', self.gym_member.name)

        # Assert that the member details are correct
        self.assertEqual(saved_gym_member.first_name, 'John')
        self.assertEqual(saved_gym_member.last_name, 'Doe')
        self.assertEqual(saved_gym_member.date_of_birth, '1990-01-01')
        self.assertEqual(saved_gym_member.gender, 'Male')
        self.assertEqual(saved_gym_member.contact_number, '1234567890')
        self.assertEqual(saved_gym_member.email, 'john.doe@example.com')
        self.assertEqual(saved_gym_member.address, '123 Main Street, City')
        self.assertEqual(saved_gym_member.emergency_contact_details, 'Emergency Contact Name: Jane, Phone: 9876543210')
        self.assertEqual(saved_gym_member.joining_date, '2024-01-01')
        self.assertEqual(saved_gym_member.height, 180.0)
        self.assertEqual(saved_gym_member.weight, 75.0)
        self.assertEqual(saved_gym_member.registration_date, '2024-01-01')

        # Add more assertions as needed

    def test_update_height_and_weight(self):
        # Update the height and weight of the Gym Member
        self.gym_member.height = 185.0
        self.gym_member.weight = 78.0
        self.gym_member.save()

        # Fetch the Gym Member to ensure the updates are reflected
        updated_gym_member = frappe.get_doc('Gym Member', self.gym_member.name)

        # Assert that the height and weight are updated
        self.assertEqual(updated_gym_member.height, 185.0)
        self.assertEqual(updated_gym_member.weight, 78.0)

        # Add more assertions as needed

if __name__ == '__main__':
    frappe.init(site='mygym.com')  # Replace with your Frappe site name
    unittest.main()
