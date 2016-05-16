# -*- coding: utf-8 -*-

from openerp import fields, models, api, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    ddt_into_invoice = fields.Boolean(_('Show Transport information on Invoice'))

    @api.model
    def _make_invoice(self, order, lines):
        inv_id = super(SaleOrder, self)._make_invoice(order, lines)

        self.env['account.invoice'].browse(inv_id).write({
            'ddt_into_invoice': order.ddt_into_invoice,
        })

        return inv_id
