# -*- coding: utf-8 -*-

from openerp import fields, models, _


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    ddt_into_invoice = fields.Boolean(_('Show Transport information on Invoice'))
