import frappe
from frappe.utils import now_datetime

@frappe.whitelist()
def heartbeat():
    """
    Updates user's 'last_active' every minute.
    Called automatically by browser JS to mark presence.
    """
    user = frappe.session.user
    if user == "Guest":
        return

    frappe.db.set_value("User", user, "last_active", now_datetime())
    frappe.db.commit()
    return {"ok": True}
