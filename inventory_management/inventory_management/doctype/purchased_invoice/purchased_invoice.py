# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PurchasedInvoice(Document):
	def before_submit(self):
		self.update_quantity()
		for i in self.items:
			# if not frappe.db.exists("Transaction Record",self.company_name):
				data = frappe.new_doc("Transaction Record")
				data.transaction_type = "Purchased Invoice"
				data.transaction_name = self.name
				data.company_name = self.company_name
				data.product_name = i.product_name
				data.party_name = "Supplier"
				data.purchased_quantity = i.order_quantity
				data.purchased_price = i.price
				data.transaction_date = i.order_date
				data.amount = i.order_quantity * i.price
				data.due_date = frappe.utils.add_to_date(i.order_date, days=+5)
				data.insert()
			
	def update_quantity(self):
		for i in self.items:
			quantity = frappe.get_doc("Products Availability",i.product_name)
			print(quantity.quantity)
			print(i.order_quantity)
			quantity.quantity = quantity.quantity + i.order_quantity
			print(quantity.quantity)
			if quantity.quantity <= 50:
				print(quantity.quantity)
				quantity.save()
				print(quantity.save())
				# self.stock_update(quantity.quantity)
			else:
				frappe.throw(f"{i.product_name} purchasing is exceeding ({quantity.quantity}) the maximum limit(50) !")

	# def stock_update(self,quantity):
	# 	for i in self.items:
	# 		i.stock_quantity = quantity
	# 		print(i.stock_quantity)
