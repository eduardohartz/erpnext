import frappe

def crm_lead_has_permission(doc, ptype, user):
    # Always allow system-level users / roles
	user_doc = frappe.get_doc('User', frappe.user)
	has_special_role = [r for r in user_doc.roles if r.role == 'System Manager']
    if user == "Administrator" or has_special_role:
        return True

    # Allow creation (even if ptype is None)
    if (ptype == "create" or ptype is None):
        return True

    # Allow if user is the owner
    if getattr(doc, "lead_owner", None) == user:
        return True

    # Otherwise deny
    return False
