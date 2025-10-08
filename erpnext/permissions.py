import frappe

def crm_lead_has_permission(doc, ptype, user):
    # Always allow administrator
    if user == "Administrator":
        return True

    # Check system manager role
    user_doc = frappe.get_doc("User", user)
    if any(r.role == "System Manager" for r in user_doc.roles):
        return True

    # Allow creation only
    if ptype == "create":
        return True

    # Allow only if user is lead owner
    if getattr(doc, "lead_owner", None) == user:
        return True

    # Otherwise deny
    return False
