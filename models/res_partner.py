from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # One2many (Many2one inverse)
    published_book_ids = fields.One2many(
        'library.book',  # related model
        'publisher_id',  # field for "this" in the related model
        string='Published Books'
    )

    # Many2many
    books_id = fields.Many2many(
        'library.book',
        string='Authored Books'
    )
