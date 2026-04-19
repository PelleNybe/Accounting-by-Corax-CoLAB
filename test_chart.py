import json

try:
    with open('/app/erpnext_sweden/erpnext_sweden/setup/se_bas_chart_of_accounts.json', 'r') as f:
        data = json.load(f)
        print("Valid JSON")
except Exception as e:
    print(f"Error: {e}")
