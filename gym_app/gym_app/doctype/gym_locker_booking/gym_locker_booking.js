// Copyright (c) 2024, Dipen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	// refresh: function(frm) {

	// }
	validate: function(frm) {

        var locker_number = frm.doc.locker_number;
		console.log(locker_number);
        
        frappe.call({
            method: 'gym_app.gym_app.doctype.gym_locker_booking.gym_locker_booking.validate_locker_booking',
            args: {
                doctype: 'Gym Locker Booking',
                filters: { 'locker_number': locker_number,'status': 'Booked' }
            },
            callback: function(response) {
                console.log(response.message)
                if (response.message) {

                    frappe.msgprint(__(response.message));
                    frappe.validated = false;
                }
            }
        });
    }
});