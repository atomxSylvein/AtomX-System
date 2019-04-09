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
	m_uom_name = fields.Selection([("day", "Jour(s)"), ("hour", "Heure(s)")], default='day', string="Unité de mesure", readonly=True)



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

		domain = [('employee_id', '=', int(rec.m_employee)), ('validated', '=', True)]

		if rec.m_date_start:
			domain.append(('date', '>=', rec.m_date_start))

		if docs.m_date_end:
			domain.append(('date', '<=', rec.m_date_end))
		"""if rec.m_date_start and rec.m_date_end:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '>=', rec.m_date_start),('date', '<=', rec.m_date_end)]
		elif rec.m_date_start:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '>=', rec.m_date_start)]
		elif docs.m_date_end:
			domain = [('employee_id', '=', int(rec.m_employee)), ('date', '<=', rec.m_date_end)]
		else:
			domain = [('employee_id', '=', int(rec.m_employee))]"""

		timesheets = timesheet_environment.search(domain, order='date asc')

		#Data recording
		records = []
		total = 0
		for t in timesheets:
			amount = t.unit_amount / t.product_uom_id.factor
			vals = {'project': t.account_id.name,
					'duration': amount,
					'task': t.task_id.name,
					'description':t.name,
					'date': t.date,}
			total += amount
			records.append(vals)

		data['employee'] = rec.m_employee.name
		data['uom'] = dict(rec._fields['m_uom_name'].selection).get(rec.m_uom_name)
		data['timesheets'] = records
		data['total'] = total

		return self.env.ref('timesheet_addon.action_timesheet_report').report_action(self, data=data, config=False)