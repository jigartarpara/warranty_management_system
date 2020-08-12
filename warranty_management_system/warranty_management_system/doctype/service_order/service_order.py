# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ServiceOrder(Document):
	def on_submit(self):
		if self.issue:
			issue = frappe.get_doc("Issue",self.issue)
			issue.status = "Warranty Claim Raised"
			issue.save(ignore_permissions=True)
