"""Filter txn sms from all the sms

Algo:
Positives:
------------------------------------------------------------------------------------
'Rs ' or 'Rs.' or 'rs ' or 'rs.' or 'INR' or 'inr'    (Required)
if not return false
------------------------------------------------------------------------------------
'credit' or 'bebit' or 'payment' or 'paid' or 'added' or 'spent' (Required)
------------------------------------------------------------------------------------

Negatives:
------------------------------------------------------------------------------------
if 'win', 'OTP' is present False
------------------------------------------------------------------------------------
"""


