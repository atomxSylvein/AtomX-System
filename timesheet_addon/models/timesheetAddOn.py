from odoo import models, fields, api
from datetime import datetime

class TimesheetAddOn(models.Model):

	_name = 'timesheet_addon.tbe'
	_description = 'Model to print timesheets'

	m_employee = fields.Many2one('hr.employee', string="Employé", required=True)
	m_date_start = fields.Date(string="Date de début", default=lambda self: fields.Date.today(), required=True)
	m_date_end = fields.Date(string="Date de fin", default=lambda self: fields.Date.today(), required=True)
	m_uom_name = fields.Selection([("day", "Jour(s)"), ("hour", "Heure(s)")], default='day', string="Unité de mesure", readonly=True)
	m_customer = fields.Many2one('res.partner', string="Client", domain="[('is_company','=',True)]")
	m_language = fields.Selection(related='m_customer.lang', string="Langue du client", store=False, readonly=True)

	@api.model
	def print_timesheet(self, data):
		"""Redirects to the report with the values obtained from the wizard
		'data['form']': name of employee and the date duration"""

		#Form reading
		rec = self.browse(data)
		data = {}
		data['form'] = rec.read(['m_employee', 'm_date_start', 'm_date_end', 'm_customer', 'm_language'])
		data['language'] = data['form'][0]['m_language']

		if data['language'] == 'fr_FR':
			data['form'][0]['m_date_start'] = data['form'][0]['m_date_start'].strftime('%d/%m/%Y')
			data['form'][0]['m_date_end'] = data['form'][0]['m_date_end'].strftime('%d/%m/%Y')
		else:
			data['form'][0]['m_date_start'] = data['form'][0]['m_date_start'].strftime('%m/%d/%Y')
			data['form'][0]['m_date_end'] = data['form'][0]['m_date_end'].strftime('%m/%d/%Y')

		#Query preparation using ORM
		timesheet_environment = self.env['account.analytic.line']

		domain = [
			('employee_id', '=', int(rec.m_employee)), 
			('validated', '=', True),
			('date', '>=', rec.m_date_start),
			('date', '<=', rec.m_date_end),
			('partner_id', '=', int(rec.m_customer))
		]

		timesheets = timesheet_environment.search(domain, order='date asc')

		#Get partner address (naive way)
		data['partner_id'] = rec.m_customer
		data['customer_name'] = rec.m_customer.name
		data['customer_street'] = rec.m_customer.street
		data['customer_street2'] = rec.m_customer.street2
		data['customer_country'] = rec.m_customer.country_id.name
		data['customer_city'] = rec.m_customer.city
		data['customer_state'] = rec.m_customer.state_id.name
		data['customer_zip'] = rec.m_customer.zip

		data['employee'] = rec.m_employee.name
		data['uom'] = dict(rec._fields['m_uom_name'].selection).get(rec.m_uom_name)


		if len(timesheets) == 0:
			data['timesheets'] = []
			data['total'] = 0
			data['error'] = "/!\\ Aucune feuille de temps valide n'a été trouvée /!\\"
			return self.env.ref('timesheet_addon.action_timesheet_report').report_action(self, data=data, config=False)

		#Data recording
		records = []
		total = 0
		for t in timesheets:
			amount = t.unit_amount / t.product_uom_id.factor

			if data['language'] == 'fr_FR':
				_date = t.date.strftime('%d/%m/%Y')
			else:
				_date = t.date.strftime('%m/%d/%Y')

			vals = {'project': t.account_id.name,
					'duration': amount,
					'task': t.task_id.name,
					'description':t.name,
					'date': _date,} 
			total += amount
			records.append(vals)

		data['timesheets'] = records
		data['total'] = total

		return self.env.ref('timesheet_addon.action_timesheet_report').report_action(self, data=data, config=False)