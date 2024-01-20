// Copyright (c) 2024, Dipen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Class Booking', {
	// refresh: function(frm) {

	// }
	on_submit: function(frm) {
        frappe.call({
            method: 'gym_app.gym_app.doctype.gym_class_booking.gym_class_booking.send_booking_confirmation_email',
            args: {
                member: frm.doc.member,
                class_type: frm.doc.class_type,
                booking_date: frm.doc.booking_date
            },
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint(__('Booking confirmation email sent successfully.'));
                }
            }
        });
    }
});
