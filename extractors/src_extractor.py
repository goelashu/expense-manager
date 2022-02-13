import re
import constants
import logging

class SourceExtractor(object):
    source_set = set()
    
    def __init__(self) -> None:
        pass
    
    def _get_last_four_digits_ac_no(self, acc_no_str):
        four_digit_acc_no = None
        try:
            four_digit_acc_no = re.findall(constants.INT_REGEX, acc_no_str)[0]
            four_digit_acc_no = four_digit_acc_no[len(four_digit_acc_no)-4:]
        except:
            logging.error('Could not get 4 digit account number from sms: {acc_no}'.format(acc_no=acc_no_str))
        return four_digit_acc_no


    def _extract_bank_name(self, sms):
        for bank_acronym in constants.BANK_ACRONYMS:
            if bank_acronym in sms.address.lower():# or bank_acronym in sms.body.lower():
                
                return bank_acronym
        return 'UNKNOWN'


    def _extract_bank_account_info(self, sms):
        bank_name = self._extract_bank_name(sms)
        for regex in constants.ACCOUNT_NUMBER_REGEX:
            match = re.search(regex, sms.body)
            if match:
                return (self._get_last_four_digits_ac_no(match.group(0)), bank_name)
        return None


    def create_source_set(self, sms_list):
        """Extracts sources from sms_list
        
        """

        # Extract bank sources
        for sms in sms_list:
            from utils import has_amount, has_spam_words
            if has_amount(sms) and not has_spam_words(sms):
                src = self._extract_bank_account_info(sms)
                if src:
                    self.source_set.add(src)


    def get_source_set(self):
        return self.source_set

    def _check_presence_of_existing_source(self, sms):
        for acc_no, bank_name in self.source_set:
            if bank_name in sms.address.lower() and acc_no in sms.body.lower():
                return (acc_no, bank_name)
        return None
    
    def extract_source(self, sms):
        # Try extracting bank info from sms
        src_info = self._extract_bank_account_info(sms)
        if src_info:
            self.source_set.add(src_info)
            return src_info
        
        # If cannot extract try to match existing sources in the sms
        src_info = self._check_presence_of_existing_source(sms)
        return src_info
        
        