import constants
import re
import logging

class AmountExtractor(object):
    # this string is used to extract float from a string
    extraction_string = '\d+.*\d*'
    
    @classmethod
    def _get_amount(cls, amount_string):
        amount = None
        try:
            amount_string = amount_string.replace(',', '')
            amount = re.findall(cls.extraction_string, amount_string)
            amount = float(amount[0])
        except ValueError:
            # To-do: Leaving the raise statment for development testing. Remove in final draft
            raise Exception('Could not convert amount from the extracted string: {amount_string}'.format(amount_string=amount_string))
            # logging.error('Could not convert amount from the extracted string: {amount_string}'.format(amount_string=amount_string))
        return amount
    
    @classmethod
    def extract_amount(cls, body):
        amount = None
        for regex in constants.RUPEES_REGEX:
            match = re.search(regex, body)
            if match:
                amount = AmountExtractor._get_amount(match.group(0))
                if amount:
                    return amount

        return amount
