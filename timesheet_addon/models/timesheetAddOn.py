from odoo import models, fields, api

"""class TimesheetSettings(models.TransientModel):
	_name = 'timesheet_addon.settings'
	_inherit = 'res.config.settings'"""

class TimesheetAddOn(models.Model):

	_name = 'timesheet_addon.tbe'
	_description = 'Model to print timesheets'

	m_employee = fields.Many2one('hr.employee', string="Employé", required=True)
	m_date_start = fields.Date(string="Date de début", required=True)
	m_date_end = fields.Date(string="Date de fin", required=True)
	#m_config = fields.Many2one('timesheet_addon.settings', string="Configuration générale", readonly=True)
	#m_config_unit = fields.Many2one(related='m_config.timesheet_encode_uom_id', string="Encodage de la durée", readonly=True)
	#m_config_unit_name = fields.Char(related='m_config_unit.name', string="Unité de mesure", readonly=True)
	m_uom_name = fields.Char(compute="_compute_uom", string="Unité de mesure", readonly=True)
	m_uom_factor = fields.Integer(string="Facteur de l'unité de mesure")

	@api.model
	def _compute_uom(self):
		"""conf_environment = self.env['ir.config_parameter'].sudo()
		config_uom = conf_environment.get_param('timesheet_encode_uom_id')[0]
		uom_name = config_uom.name
		for tao in self:
			tao.m_uom_name = uom_name"""
		self.m_uom_name = "Hello World !"


	@api.model
	def print_timesheet(self, data):
		"""Redirects to the report with the values obtained from the wizard
		'data['form']': name of employee and the date duration"""

		#Form reading
		rec = self.browse(data)
		data = {}
		data['form'] = rec.read(['m_employee', 'm_date_start', 'm_date_end'])

		#Query preparation using ORM
		timesheet_environment = self.env['account.analytic.line']

		if rec.m_date_start and rec.m_date_end:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '>=', rec.m_date_start),('date', '<=', rec.m_date_end)]
		elif rec.m_date_start:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '>=', rec.m_date_start)]
		elif docs.m_date_end:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '<=', rec.m_date_end)]
		else:
			domain = [('employee_id', '=', int(rec.m_employee))]

		timesheets = timesheet_environment.search(domain, order='date asc')

		#Data recording
		records = []
		total = 0
		for t in timesheets:
			vals = {'project': t.account_id.name,
					'duration': t.unit_amount / t.product_uom_id.factor,
					'task': t.task_id.name,
					'description':t.name,
					'date': t.date,}
			total += t.unit_amount
			records.append(vals)

		data['employee'] = rec.m_employee.name
		data['unit'] = rec.m_config_unit_name
		data['timesheets'] = records
		data['total'] = total

		return self.env.ref('timesheet_addon.action_timesheet_report').report_action(self, data=data, config=False)