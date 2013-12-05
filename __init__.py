# This file is part of account_payment_bank module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .payment import *


def register():
    Pool.register(
        Journal,
        Group,
        Payment,
        module='account_payment_bank', type_='model')
    Pool.register(
        PayLine,
        module='account_payment_bank', type_='wizard')
