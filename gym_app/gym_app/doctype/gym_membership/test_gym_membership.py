# Copyright (c) 2024, Dipen and Contributors
# See license.txt

import frappe
import unittest
from frappe.utils import now

class TestGymMembership(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")  # Set a test user
        frappe.db.sql("DELETE FROM `tabMembership`")  # Clear existing records
        frappe.db.sql("DELETE FROM `tabGym Member`")  # Clear existing gym members
        frappe.db.sql("DELETE FROM `tabMembership Plan`")  # Clear existing membership plans
        frappe.db.commit()

        # Create a test gym member
        self.gym_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "John",
            "last_name": "Doe",
        })
        self.gym_member.insert()

        # Create a test membership plan
        self.membership_plan = frappe.get_doc({
            "doctype": "Membership Plan",
            "plan_name": "Gold Plan",
            "amount": 100,
        })
        self.membership_plan.insert()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def test_valid_membership_creation(self):
        # Test case for creating a membership with valid data
        membership_data = {
            "member": self.gym_member.name,
            "membership_type": self.membership_plan.name,
            "start_date": now(),
        }

        membership = frappe.get_doc({"doctype": "Membership", **membership_data})
        membership.insert()

        self.assertIsNotNone(membership.name)

    def test_missing_required_fields(self):
        # Test case for creating a membership with missing required fields
        membership_data = {
            "member": self.gym_member.name,
        }

        membership = frappe.get_doc({"doctype": "Membership", **membership_data})

        with self.assertRaises(frappe.ValidationError):
            membership.insert()

    def test_valid_payment_status(self):
        # Test case for setting a valid payment status
        membership_data = {
            "member": self.gym_member.name,
            "membership_type": self.membership_plan.name,
            "start_date": now(),
            "payment_status": "Complete",
        }

        membership = frappe.get_doc({"doctype": "Membership", **membership_data})
        membership.insert()

        self.assertEqual(membership.payment_status, "Complete")


if __name__ == '__main__':
    unittest.main()
