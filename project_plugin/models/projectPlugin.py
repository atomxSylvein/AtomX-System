from odoo import models, fields, api

class ProjectPlugin(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_description (str): A manual description about the project
	    m_typologie (selection): Describe the type of business
	"""
	
	_inherit = 'project.project'
	m_description = fields.Text(string="Description du projet")
	m_typology = fields.Selection(	[('4', 'Services Développement'), ('1', 'Services Intégration ServiceNow'), ('191', 'Services Intégration Odoo'), ('0', 'Autres')], string="Business Unit Service")