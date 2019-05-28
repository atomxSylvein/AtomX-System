from odoo import models, fields, api

class SaleOrderPlugin(models.Model):

	"""This class extends Order class and provides sage invoice number (for older sale orders)
	
	Attributes:
	    m_sage_number (str): Invoice Sage number
	"""
	
	_inherit = 'sale.order'
	m_sage_number = fields.Char(string="Sage N°")

