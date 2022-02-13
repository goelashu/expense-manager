class SMS(object):
    address = None
    timestamp = None
    body = None

    def __init__(self, address, timestamp, body):
        self.address = address
        self.timestamp = timestamp
        self.body = body
    
    def __str__(self):
        print(self.address, self.timestamp)
        return 'address: {address}, timestamp: {timestamp}, body: "{body}"'.format(
                    address=self.address,
                    timestamp=self.timestamp,
                    body=self.body
                )