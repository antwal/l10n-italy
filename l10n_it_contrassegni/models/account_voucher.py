# -*- coding: utf-8 -*-

from openerp.osv import osv


class AccountMoveReconcile(osv.osv):
    _inherit = "account.move.reconcile"

    def _check_same_partner(self, cr, uid, ids, context=None):
        same_partner = super(AccountMoveReconcile, self)._check_same_partner(cr, uid, ids, context=context)
        return same_partner if same_partner else self._check_cash_on_delivery_payment(cr, uid, ids, context=context)

    def _check_cash_on_delivery_payment(self, cr, uid, ids, context=None):
        for reconcile in self.browse(cr, uid, ids):
            if not reconcile.opening_reconciliation:
                if reconcile.line_id and reconcile.line_id[0].journal_id.cash_on_delivery_payment:
                    return True
                elif reconcile.line_partial_ids and reconcile.line_partial_ids[0].journal_id.cash_on_delivery_payment:
                    return True

        return False

    _constraints = [
        (_check_same_partner,
         'You can only reconcile journal items with the same partner.',
         ['line_id', 'line_partial_ids']),
    ]
