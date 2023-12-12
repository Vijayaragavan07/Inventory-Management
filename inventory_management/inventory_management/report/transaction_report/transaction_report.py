# Copyright (c) 2023, Vijayaragavan and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
	columns, data = get_columns(filters),get_data(filters)
	print(columns)
	print(data)
	return columns,data
def get_columns(filters):
	columns = [
		{
			"label" : _("Transaction Record"),
			"fieldtype" : "Link",
			"fieldname" : "name",
			"options" : "Transaction Record",
		},
		{
			"label" : _("Product Name"),
			"fieldtype" : "Link",
			"fieldname" : "product_name",
			"options" : "Transaction Record",
		},
		{
			"label" : _("Transaction Name"),
			"fieldtype" : "Select",
			"fieldname" : "transaction_name",
			"options" : ["Supplier","Customer"],
		},
		{
			"label" : _("Amount"),
			"fieldtype" : "Currency",
			"fieldname" : "amount",
		},
		{
			"label" : _("Company Name"),
			"fieldtype" : "Link",
			"fieldname" : "company_name",
			"options" : "Company",
		},
		{
			"label":_("Transaction Type"),
			"fieldtype":"Select",
			"fieldname":"transaction_type",
			"options":["Selling Invoice","Purchased Invoice"]
		},
		{
			"label":_("Transaction Date"),
			"fieldtype":"DateTime",
			"fieldname":"transaction_date",
		},
		{
			"label":_("Party Name"),
			"fieldtype":"Select",
			"fieldname":"party_name",
			"options":["Customer","Supplier"]
		},
		{
			"label":_("Sold Price"),
			"fieldtype":"Currency",
			"fieldname":"selled_price"
		},
		{
			"label":_("Sold Quantity"),
			"fieldtype":"Float",
			"fieldname":"selled_quantity"
		},
		{
			"label":_("Purchased Price"),
			"fieldtype":"Currency",
			"fieldname":"purchased_price"
		},
		{
			"label":_("Purchsed Quantity"),
			"fieldtype":"Float",
			"fieldname":"purchased_quantity"
		},
		{
			"label":_("Due Date"),
			"fieldtype":"Date",
			"fieldname":"due_date"
		}
	]
	return columns

def get_data(filters):
	data = []
	filter ={}
	reference_doctype = filters.get("reference_doctype")
	reference_name = filters.get("reference_name")	

	if reference_name:
		filter = {"name":reference_name}
	
	reference_list = frappe.get_list(reference_doctype,filters = filter, fields = ["name","product_name","transaction_name","amount","company_name","transaction_type","transaction_date","party_name","selled_price","selled_quantity","purchased_price","purchased_quantity","due_date"], as_list=True)

	result = []

	for i in reference_list:
		data = list(i)
		result.append(data)
	print(result)
	return result