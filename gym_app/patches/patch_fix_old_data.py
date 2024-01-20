import frappe

def execute():
    # Fetch all Gym Members without the new field set
    members_without_new_field = frappe.get_all("Gym Member", filters={"full_name": None}, fields=["name"])

    for member in members_without_new_field:
        # Get some data from existing fields to set in the new field
        # For example, concatenating First Name and Last Name
        full_name = frappe.get_value("Gym Member", member.name, ["first_name", "last_name"], as_dict=True)
        new_value = f"{full_name.get('first_name')} {full_name.get('last_name')}"

        # Set the new value in the new field
        frappe.db.set_value("Gym Member", member.name, "full_name", new_value)