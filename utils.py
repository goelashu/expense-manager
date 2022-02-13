from detectors.regex import bank_regex
import constants 
import re

def regex_match(row):
    for regex in bank_regex['HDFC']:
        match = re.search(regex, row['body'])
        if match:
            return True
    return False

def is_bank_address(sms):
    for bank_acronym in constants.BANK_ACRONYMS:
        if bank_acronym in sms.address.lower():
            return True
    return False

def has_amount(sms):
    for regex in constants.RUPEES_REGEX:
        match = re.search(regex, sms.body)
        if match:
            return True
    
    return False
    
def has_spam_words(sms):
    for spam_word in constants.SPAM_WORDS:
        if spam_word in sms.body.lower():
            return True
    return False

def is_false_positive(sms):
    return not has_amount(sms) or has_spam_words(sms)
        