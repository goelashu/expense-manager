from enum import Enum

class DestType(object):
    UPI = 'UPI'
    BANK = 'BANK'
    MERCHANT = 'MERCHANT'

class Destination(object):
    address = None # UPI address/ bank acc no
    ref_no = None # UPI ref_no / Any id from merchant
    merchant = None # merchant name
    type = None # UPI/Merchant (Pick from DestType)
    
    def __init__(self, address=None, ref_no=None, merchant=None, type=None):
        self.address = address
        self.ref_no = ref_no
        self.merchant = merchant
        self.type = type
    
    def __str__(self):
        return 'address: {address}, ref_no: {ref_no}, merchant: {merchant},type: {type}'.format(
            address=self.address,
            ref_no=self.ref_no,
            merchant=self.merchant,
            type=self.type
        )
    