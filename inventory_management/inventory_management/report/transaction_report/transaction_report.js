// Copyright (c) 2023, Vijayaragavan and contributors
// For license information, please see license.txt

frappe.query_reports["Transaction Report"] = {
	"filters": [
		{
			reqd : 1,
			fieldname:"reference_doctype",
			label: __("Entity type"),
			fieldtype: "Link",
			options: "DocType",
			// default : null,
			get_query:function(){
				return{
					filters: {
						name:["in","Transaction Record"]
					},
				}
			},
		},
		{
			fieldname:"reference_name",
			label:__("Entity Name"),
			fieldtype:"Dynamic Link",
			get_options:function(){
				let ref_doctype = frappe.query_report.get_filter_value("reference_doctype")
				if(!ref_doctype){
					frappe.throw("Please select the doctype first!")
				}
				return ref_doctype
			}
		}
	]
};
