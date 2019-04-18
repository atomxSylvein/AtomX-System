from odoo import api, models

class TimesheetReport(models.AbstractModel):
    _name = 'report.timesheets_by_employee.report_timesheet'
    _description = 'Timesheet report'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('timesheets_by_employee.report_timesheet')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render('timesheets_by_employee.report_timesheet', docargs)