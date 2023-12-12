# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document


class SellingInvoice(Document):
	def before_submit(self):
		for i in self.items:
			# if not frappe.db.exists("Transaction Record",self.customer_name):
				data = frappe.new_doc("Transaction Record")
				quantity = frappe.get_doc("Products Availability",i.product_name)
				if i.out_quantity <= quantity.quantity:
					data.transaction_type = "Selling Invoice"
					data.transaction_name = self.name
					data.product_name = i.product_name
					data.company_name = self.company_name
					data.customer_name = self.customer_name
					data.party_name = "Customer"
					data.selled_quantity = i.out_quantity
					data.selled_price = i.price
					data.transaction_date = self.selling_date
					data.amount = i.price * i.out_quantity
					data.due_date= frappe.utils.add_to_date(self.selling_date, days=+5)
					data.insert()
					self.update_quantity()
				else:
					frappe.throw(f"Please enter valid out_quantity level ! (Max qty = {quantity.quantity})")

	def update_quantity(self):
		# for item in self.items:
		# 	if frappe.db.exists("Products Availability",{"name":item.product_name}):
		# 		doc = frappe.get_doc("Products Availability",item.product_name)
		# 		doc.quantity -= item.out_quantity
		# 		doc.save()
				# frappe.db.set_value("Products Availability",{"name":item.product_name},"quantity",10)
		for i in self.items:
			quantity = frappe.get_doc("Products Availability",i.product_name)
			print(quantity.name)
			print(quantity.quantity)
			if quantity.quantity > 0:
				print("true")
				quantity.quantity = quantity.quantity - i.out_quantity
				print(quantity.quantity)
				quantity.save()
				print(quantity.save())
				# self.stock_update(quantity.quantity)
			else:
				frappe.throw(f"{i.product_name} not available!")

	# def stock_update(self,quantity):
	# 	for i in self.items:
	# 		i.stock_quantity = quantity
