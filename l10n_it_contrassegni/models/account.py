# -*- coding: utf-8 -*-

from openerp import models, fields, api, _


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    cash_on_delivery_payment = fields.Boolean(help=_("Allow Cash on delivery payments with this journal"))
    carrier_id = fields.Many2one('delivery.carrier', _('Carrier'))


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    cash_on_delivery_partner_id = fields.Many2one('res.partner', _('Cash On Delivery Partner'))


class AccountVoucher(models.Model):
    _inherit = 'account.voucher'

    @api.model
    def create_first_line(self, voucher, move_id, company_currency, current_currency):
        move_line = super(AccountVoucher, self).create_first_line(voucher, move_id, company_currency, current_currency)

        if voucher.journal_id.cash_on_delivery_payment:
            # This payment is with cash on delivery,
            #  then i have to change the partner
            move_line.write({
                'name': move_line.name + voucher.partner_id.name,
                'partner_id': voucher.journal_id.carrier_id.partner_id.id,
                'cash_on_delivery_partner_id': voucher.partner_id.id
            })

        return move_line
