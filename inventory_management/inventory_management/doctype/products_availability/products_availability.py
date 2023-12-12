# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ProductsAvailability(Document):
    pass
	# def after_save(self):
	# 	exists = frappe.db.exists(
	# 		"Products Availability",
	# 		{
	# 			"product_name":self.product_name
	# 		}
	# 	)
	# 	if exists:
	# 		quantity = frappe.get_doc("Products Availability",exists)
	# 		quantity.quantity += self.quantity
		
