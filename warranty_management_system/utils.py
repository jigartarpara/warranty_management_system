import frappe
from frappe.utils import now_datetime

def validate_issue(doc, method):
	
	if doc.item_receipt:
		if not doc.item_receipt_date:
			doc.item_receipt_date = now_datetime()	
	else:
		doc.item_receipt_date = ""
	
	if doc.item_delivery:
		if not doc.item_delivery_date:
			doc.item_delivery_date = now_datetime()
	else:
		doc.item_delivery_date = ""