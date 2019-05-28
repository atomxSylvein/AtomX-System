from odoo import models, fields, api

class InvoicePlugin(models.Model):

	"""This class extends Invoice class and provides sage invoice number (for older invoices)
	
	Attributes:
	    m_sage_number (str): Invoice Sage number
	"""
	
	_inherit = 'account.invoice'
	m_sage_number = fields.Char(string="Sage N°")