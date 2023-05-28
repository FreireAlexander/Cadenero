from account import Account

class Car(Account):
    id = int
    license = str
    passenger = str

    def __init__(self, Account, license):
        super(Car, self).__init__(Account.name, Account.document)
        self.license = license
        
        