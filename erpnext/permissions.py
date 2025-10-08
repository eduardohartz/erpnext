# erpnext/permissions.py
import frappe

def crm_lead_has_permission(doc, ptype, user):
    # always allow system-level users
    if user == "Administrator" or frappe.has_role(user, "System Manager"):
        return True

    # allow if the user is the lead owner
    if getattr(doc, "lead_owner", None) == user:
        return True

    # allow if explicitly shared
    if frappe.db.exists("Share", {"parent": doc.name, "user": user}):
        return True

    # deny otherwise
    return False
