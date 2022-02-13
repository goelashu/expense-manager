"""This file contains regex for parsing sms mapped according to banks
"""
    
bank_regex = {
    'HDFC': [
        # 'Rs (.+?) debited from a/c (.+?) .* to (.+?)\..*',
        # 'Rs. (.+?) debited from a/c (.+?) .* to (.+?)\..*',
        'Rs. (.+?) credited to a/c (.+?) .*by a/c linked to (.+?)\..*'
    ]
}