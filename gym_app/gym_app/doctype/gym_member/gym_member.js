// Copyright (c) 2024, Dipen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
    refresh: function(frm) {
        // Your code for the onload event

        // Example: Set a default value for a field
        frm.set_value('registration_date', frappe.datetime.nowdate());

        // Example: Add a custom button to subscribe to a gym plan
        frm.add_custom_button(__('Subscribe to Gym Plan'), function() {
            frappe.set_route('List', 'Gym Membership', {'filters': {'member': frm.doc.name}});
        });
    },

	validate: function(frm) {
        if (frm.doc.contact_number) {
            validateContactNumberFormat(frm.doc.contact_number);
        }
        if(frm.doc.emergency_contact_details){
            validateContactNumberFormat(frm.doc.emergency_contact_details);
        }
        calculateBMI(frm);
    }

   
});

function calculateBMI(frm) {
    var height = frm.doc.height;
    var weight = frm.doc.weight;

    if (height && weight) {
        // Formula for BMI: weight (kg) / (height (m) * height (m))
        var bmi = weight / (height * height);

        // Round the BMI to two decimal places
        bmi = parseFloat(bmi.toFixed(2));

        // Set the calculated BMI in the 'bmi' field
        frm.set_value('bmi', bmi);
    }
}
function validateContactNumberFormat(contactNumber) {
    // Add your client-side contact number format validation logic here
    // For example, a simple check for 10 digits
    if (!/^\d{10}$/.test(contactNumber)) {
        frappe.msgprint(__("Please enter a valid 10-digit contact number"));
        frappe.validated = false;
    }
}