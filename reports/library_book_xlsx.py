from odoo import models


class LibraryBookXLSX(models.AbstractModel):
    _name = 'report.library_app.book_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, record):
        # for obj in partners:
        #     report_name = obj.name
        #     # One sheet by partner
        #     sheet = workbook.add_worksheet(report_name[:31])
        #     bold = workbook.add_format({'bold': True})
        #     sheet.write(0, 0, obj.name, bold)

        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Book')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, record.name)

