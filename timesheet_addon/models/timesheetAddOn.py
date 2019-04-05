from odoo import models, fields, api

class TimesheetAddOn(models.Model):

	_name = 'timesheets_by_employee.timesheets_by_employee'
	_description = 'Model to print timesheets'

	m_employee = fields.Many2one('hr.employee', string="Employé", required=True)
	m_date_start = fields.Date(string="Date de début", required=True)
	m_date_end = fields.Date(string="Date de fin", required=True)

	@api.model
    def print_timesheet(self, data):
		"""Redirects to the report with the values obtained from the wizard
		'data['form']': name of employee and the date duration"""
		rec = self.browse(data)
		data = {}
		data['form'] = rec.read(['m_employee', 'm_date_start', 'm_date_end'])
		#report_obj = self.env['report']
		#report_doc = report_obj.get_action(self.browse(data), 'timesheets_by_employee.report_timesheets', data=data)
		#report_doc = report_obj._get_report_from_name('timesheets_by_employee.report_timesheets')

		return self.env.ref('timesheets_by_employee.report_timesheet').report_action(self, data=data, config=False)