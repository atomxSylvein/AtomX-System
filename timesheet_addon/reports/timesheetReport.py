from odoo import models, fields, api

class TimesheetReport(models.AbstractModel):

	_name = 'report.timesheet_addon.timesheet_report' 
	_description = 'Monthly resource cost report'

	@api.model
	def _get_report_values(self, docids, data=None):
		model = self.env.context.get('active_model')
		docs = self.env[model].browse(self.env.context.get('active_id'))

		"""get_periods, months, total_mnths = self.get_periods(data['form'])
		get_employee = self.get_employee(data['form'], months, total_mnths)
		get_months_tol = self.get_months_tol()
		get_total = self.get_total(get_months_tol)"""

		return {
		'doc_ids': docids,
		'doc_model': model,
		'data': data,
		'docs': docs
		}