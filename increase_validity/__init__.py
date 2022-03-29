import frappe
import datetime

__version__ = '0.0.1'

@frappe.whitelist()
def increase(doctype, docname):
    frappe.db.set_value(doctype, docname, 'valid_till', datetime.datetime.now())
    frappe.db.set_value(doctype, docname, 'status', "Open")
    frappe.db.commit()