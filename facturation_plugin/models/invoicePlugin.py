from odoo import models, fields, api

class InvoicePlugin(models.Model):

	"""This class extends Sale class and provides sage invoice number (for older invoices)
	
	Attributes:
	    m_sage_number (str): Invoice Sage number
	"""
	
	_inherit = 'sale.order'
	m_sage_number = fields.Char(string="Sage N°")