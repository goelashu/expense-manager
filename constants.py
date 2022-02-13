BANK_ACRONYMS = ['hdfc', 'icici','sbi', 'union', 'equt', 'axis']

RUPEES_REGEX = [
    '(?i)(?:(?:RS|INR|MRP)[\.\:]?\s?)(\d+(:?\,\d+)?(\,\d+)?(\.\d{1,2})?)',
]

# Assuming UPI does not contain capital letters
# it could still lead to issue in extraction in cases Train-myupiid@randombk converts to rain-myupiid@randombk
# leaving this problem for now to avoid loss of information.
# TODO: fix the above problem later
UPI_REGEX = '[a-z0-9.\-_]{2,256}@[a-zA-Z]{2,64}'

UPI_REF_NO_REGEX = '\d{12}'

MERCHANT_LIST = [
    'swiggy',
    'amazon',
    'flipkart',
    'mmt',
    'makemytrip',
    'make-my-trip'
]

SPAM_WORDS = ['otp', 'win']

ACCOUNT_NUMBER_REGEX = [
    '[a|A]/[c|C].*[Xx\*\.]+[0-9]{3,}',
    '[a|A]/[c|C].*[0-9]{3,}',
]

INT_REGEX = '\d+'

DEST_AC_NO_REGEX = '[Xx\*\.]+([0-9]{3,})'

TYPE_LIST = ['debited', 'credited', 'withdrawn']

SOURCE_FINDER_WORD = {
    'debited': ['from', 'for'],
    'credited': ['for', 'to', 'with', 'on', 'into'],
    'withdrawn': ['from', 'via'],
    'spent': ['on', 'from', 'via'],
    
}