"""Contains all the conditions to be met for a sms to be a transaction.
"""

from utils import is_bank_address

def contains_rs(sms):
    return 'Rs' in sms.body or 'INR' in sms.body

DEBIT_SYNONYM = ['debit', 'debited', 'payment', 'paid']
CREDIT_SYNONYM = ['credit', 'credited', 'added']

def conatins_credit_or_debit(sms):
    for debit_synonym in DEBIT_SYNONYM:
        if debit_synonym in sms.body:
            return True
    
    for credit_synonym in CREDIT_SYNONYM:
        if credit_synonym in sms.body:
            return True
    return False

def contains_a_c(sms):
    return 'a/c' in sms.body.lower()


CONDITIONS = [
    is_bank_address,
    contains_rs,
    conatins_credit_or_debit,
    contains_a_c
]