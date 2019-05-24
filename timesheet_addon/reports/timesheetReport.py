from odoo import models, fields, api

class TimesheetReport(models.AbstractModel):

	_name = 'report.timesheet_addon.timesheet_report' 
	_description = 'Monthly resource cost report'

	@api.model
	def _get_report_values(self, docids, data=None):
		model = self.env.context.get('active_model')
		docs = self.env[model].browse(self.env.context.get('active_id'))

		return {
		'doc_ids': docids,
		'doc_model': model,
		'data': data,
		'timesheets':data['timesheets'],
		'uom':data['uom'],
		'employee':data['employee'],
		'total':data['total'],
		'docs': docs
		}