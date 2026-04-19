import re

with open('/app/erpnext/accounts/doctype/account/chart_of_accounts/chart_of_accounts.py', 'r') as f:
    content = f.read()

# I want to avoid modifying erpnext.
# The prompt says: "DO NOT modify the core ERPNext or Frappe code. Instead, your task is to create a new custom Frappe application named erpnext_sweden."
