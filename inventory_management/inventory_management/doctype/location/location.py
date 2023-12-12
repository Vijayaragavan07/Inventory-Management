# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document


class Location(Document):
    pass
	# def before_save(self):
	# 	exists = frappe.db.exists(
	# 		"Location",
	# 		{
	# 			"product_name":self.product_name,
	# 			"location":self.location,
	# 		},
	# 	)
	# 	if exists:
	# 		frappe.throw("Product already added in this location !")
	# 	else:
	# 		self.validate_available()
	# 		self.update_quantity()

	# def validate_available(self):
	# 	quantity = frappe.get_doc("Products",self.product_name)
	# 	if quantity.quantity < self.quantity:
	# 		print(quantity.quantity)
	# 		total = f"Product maximum limit is {quantity.quantity}"
	# 		frappe.throw(total)

	# def update_quantity(self):
	# 	quantity = frappe.get_doc("Products",self.product_name)
	# 	print(quantity.quantity)
	# 	quantity.quantity = quantity.quantity - self.quantity
	# 	print(quantity.quantity)
	# 	quantity.save()