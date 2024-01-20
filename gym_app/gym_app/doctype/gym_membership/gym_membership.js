// Copyright (c) 2024, Dipen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	refresh: function(frm) {
        // Trigger end date calculation when the 'start_date' field changes
        frm.fields_dict['start_date'].$input.on('change', function() {
            calculateEndDate(frm);
        });
    }

});

function calculateEndDate(frm) {
    var startDate = frm.doc.start_date;

    if (startDate) {
        // Calculate end date by adding one month to the start date
        var endDate = frappe.datetime.add_months(startDate, 1);

        // Set the calculated end date in the 'end_date' field
        frm.set_value('end_date', endDate);
    }
}