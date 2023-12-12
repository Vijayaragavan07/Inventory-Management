# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document


class ProductMovement(Document):
	def before_submit(self):
		if self.status == "Departed":
			quantity = frappe.get_doc("Products Availability",self.product_name)
			if quantity.quantity >=self.quantity:
				quantity.quantity -= self.quantity
				quantity.save()
				msg =f"Quantity {self.quantity} decreased in Products Availability doctype"
				frappe.msgprint(msg)
			else:
				frappe.throw("Quantity is exceed than the availabilty!")
		elif self.status == "Delivered":
			exists = frappe.db.exists(
				"ProductMovement",
				{
					"product_name":self.product_name,
					"from_location":self.from_location,
					"to_location":self.to_location,
					"docstatus":DocStatus.submitted()
				}
			)
			if exists:
				position = frappe.get_doc("ProductMovement",exists)
				if (self.from_location == position.from_location) & (self.to_location == position.to_location) & (position.status == "Departed"):
					quantity = frappe.get_doc("Products Availability",self.product_name)
					quantity.quantity += self.quantity
					quantity.save()
					msg = f"Quantity {self.quantity} increased in Products Availability doctype"
					frappe.msgprint(msg)
			elif not exists:
				frappe.throw("Undeparted product cannot be deliverd! Departed first")
