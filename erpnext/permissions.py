import frappe

def crm_lead_has_permission(doc, ptype, user):
    # Always allow system-level users / roles
	roles = frappe.get_roles(user)
    if user == "Administrator" or "System Manager" in roles:
        return True

    # Allow creation (even if ptype is None)
    if (ptype == "create" or ptype is None):
        return True

    # Allow if user is the owner
    if getattr(doc, "lead_owner", None) == user:
        return True

    # Otherwise deny
    return False
