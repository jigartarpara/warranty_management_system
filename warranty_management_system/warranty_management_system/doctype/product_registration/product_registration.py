# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import add_days

class ProductRegistration(Document):
	def validate(self):
		if self.purchase_date and self.serial_no:
			validity = frappe.get_value("Serial No",self.serial_no, "warranty_period")
			expiry_date = add_days(self.purchase_date, validity)
			self.warranty_expiry_date = expiry_date

			serial_no = frappe.get_doc("Serial No",self.serial_no )
			serial_no.warranty_expiry_date = self.warranty_expiry_date
			serial_no.save(ignore_permissions=1)
			
