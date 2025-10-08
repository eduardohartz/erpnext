import frappe

def crm_lead_has_permission(doc, ptype, user):
    # Always allow Administrator
    if user == "Administrator":
        return True

    # Check if user has exempt roles
    user_doc = frappe.get_doc("User", user)
    if any(r.role in ("System Manager", "Sales Manager") for r in user_doc.roles):
        return True

    # Allow creation
    if ptype == "create":
        return True

    # Allow only if user is lead owner (compare as strings)
    lead_owner = getattr(doc, "lead_owner", None)
    if not lead_owner:
        # Fallback: try to get from database if doc is partial
        lead_owner = frappe.db.get_value("CRM Lead", doc.name, "lead_owner")

    if lead_owner and lead_owner == user:
        return True

    # Otherwise deny
    return False
	
