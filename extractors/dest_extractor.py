import constants
import re
import logging
from models.destination import Destination, DestType

class DestinationExtractor(object):
    def _extract_upi_ref_no(self, sms):
        upi_ref_no = None
        try:
            match_upi_ref_no = re.search(constants.UPI_REF_NO_REGEX, sms.body)
            upi_ref_no = match_upi_ref_no.group(0)
        except:
            logging.error('Could not find upi info: {no}'.format(no=upi_ref_no))
        return upi_ref_no
    
    def _clean_upi_address_string(self, upi_addr):
        """ Cleaning the following:
        1) Remove leading '-'
        """
        if upi_addr[0] == '-':
            return upi_addr[1:]
        return upi_addr
    
    def _extract_upi_address(self, sms):
        upi_addr = None
        try:
            match_upi_addr = re.search(constants.UPI_REGEX, sms.body)
            upi_addr = match_upi_addr.group(0)
            upi_addr = self._clean_upi_address_string(upi_addr)
        except:
            # TODO: change exception to error in final draft
            logging.error('Could not find upi info: {addr}'.format(addr=upi_addr))
        return upi_addr
           
     
    def _extract_merchant_name(self, sms):
        for merchant_name in constants.MERCHANT_LIST:
            if merchant_name in sms.body.lower():
                return merchant_name
        return None
    
    
    def _extract_dest_bank_info(self, sms):
        dest_acc_no = None
        try:
            for acc_no_regex in constants.ACCOUNT_NUMBER_REGEX:
                match = re.search(acc_no_regex, sms.body)
                if match:
                    bank_account_string = match.group(0)
                    bank_acc_nos = re.findall(constants.DEST_AC_NO_REGEX, bank_account_string)
                    if len(bank_acc_nos) == 2:
                        dest_acc_no = bank_acc_nos[1]
        except:
            logging.error('Cannot find destination a\c number')
        return dest_acc_no


    def extract_destination(self, sms):
        try:
            # In case of UPI destination
            upi_addr = self._extract_upi_address(sms)
            
            # try to find the names of existing merchants in sms body
            # For now assuming, merchant txn do not give ref no (Can be added later)
            merchant_name = self._extract_merchant_name(sms)
            if upi_addr or 'upi' in sms.body.lower():
                upi_ref_no = self._extract_upi_ref_no(sms)
                dest = Destination(address=upi_addr,
                                   ref_no=upi_ref_no,
                                   merchant=merchant_name,
                                   type=DestType.UPI)
                return dest
                
            # If bank is destination
            dest_acc_no = self._extract_dest_bank_info(sms)
            
            if dest_acc_no:
                # Even if bank is destination can contain upi ref no
                upi_ref_no = self._extract_upi_ref_no(sms)
                dest = Destination(address=dest_acc_no,
                                   ref_no=upi_ref_no,
                                   merchant=merchant_name,
                                   type=DestType.BANK)
                return dest
            
            if merchant_name:
                dest = Destination(address=merchant_name,
                                   type=DestType.MERCHANT)
                return dest
        except:
            logging.error('Could not find any destination: ', sms)

        return None
        