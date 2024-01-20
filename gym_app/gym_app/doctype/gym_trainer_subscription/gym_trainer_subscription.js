// Copyright (c) 2024, Dipen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer Subscription', {
	refresh: function(frm) {
        // Add a custom button to rate the trainer
        frm.add_custom_button(__('Rate Trainer'), function() {
            frappe.prompt([
                {'fieldname': 'rating', 'fieldtype': 'Int', 'label': 'Rating', 'reqd': 1},
                {'fieldname': 'feedback', 'fieldtype': 'Text', 'label': 'Feedback'}
            ],
            function(values){
                frappe.call({
                    method: 'my_app.api.rate_trainer',
                    args: {
                        trainer_subscription: frm.doc.name,
                        rating: values.rating,
                        feedback: values.feedback
                    },
                    callback: function(response) {
                        if (response.message === 'success') {
                            frappe.msgprint(__('Trainer rated successfully.'));
                        } else {
                            frappe.msgprint(__('Failed to rate trainer. Please try again.'));
                        }
                    }
                });
            },
            __('Rate Trainer'), 'Submit');
        });
    }
});
