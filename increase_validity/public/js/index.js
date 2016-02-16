frappe.ui.form.on('Quotation', {
    refresh: async (frm) => {
        if (!frm.__islocal && frm.doc.status === "Expired") {
            frm.add_custom_button('Add Validity', async () => {
                await frappe.call({
                    "method": "increase_validity.increase",
                    "type": "POST",
                     args: {
                         "doctype": frm.doc.doctype,
                         "docname": frm.doc.name
                     },
                    freeze: false,
                })
                
                frappe.show_alert("Validity Increased")
                frm.reload_doc()
            })
        }
    }
})