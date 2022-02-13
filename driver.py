"""
Driver class
"""
import xml.etree.ElementTree as ET
import os

from numpy import source

from models.sms import SMS
import pandas as pd
from utils import regex_match

def get_sms_list():
    # file_path = os.environ.get('SMS_FILE')
    file_path = '/Users/ashutoshgoel/workspace/expense_manager_workspace/data.xml'
    root = ET.parse(file_path).getroot()
    sms_list = []
    for child in root:
        sms = SMS(
            address=child.attrib['address'],
            timestamp=child.attrib['date'],
            body=child.attrib['body']
        )
        sms_list.append(sms)
    
    return sms_list

def get_dataframe(sms_list):
    sms_dict_list = []
    for sms in sms_list:
        sms_dict_list.append(
            {
                'address': sms.address,
                'timestamp': sms.timestamp,
                'body': sms.body
            }
        )
    
    sms_df = pd.DataFrame(sms_dict_list, columns=['address', 'timestamp', 'body'])
    return sms_df

sms_list = get_sms_list()
sms_df = get_dataframe(sms_list)
# match = sms_df.apply(regex_match, axis=1)
# sms_df = sms_df[match]
# sms_df = sms_df.sort_values(by=['timestamp'], ascending=False)
# print(sms_df.head(20)['body'])

from extractors.amount_extractor import AmountExtractor
from extractors.src_extractor import SourceExtractor
from extractors.dest_extractor import DestinationExtractor
from utils import is_false_positive
src_extractor = SourceExtractor()
src_extractor.create_source_set(sms_list)
dest_extractor = DestinationExtractor()


for sms in sms_list:
    amount  = AmountExtractor.extract_amount(sms.body)
    if amount and not is_false_positive(sms):
        src = src_extractor.extract_source(sms)
    # if 'ambeysales' in sms.body and 'Call' not in sms.body:
    #     # src = src_extractor.extract_source(sms)
    #     print(sms.body)
    #     print(amount)
    #     print(src)
    if amount and not is_false_positive(sms) and src:
        if src[1] == 'hdfc':# and 'Rs 138.00 debited from a/c **4723 on 22-01-22 to VPA swiggystores@icici(UPI Ref No 202230217377). Not you? Call on 18002586161 to report' in sms.body:
            dest = dest_extractor.extract_destination(sms)
            print(sms.address, sms.body)
            print('amount extracted is :',amount)
            print('source is : {source}'.format(source=src))
            print('destination is: {destination}'.format(destination=dest))
            print('\n')
    
# print(src_extractor.get_source_set())