class Person():
    def __init__(self, name):
        self.name=name
        self.payment=0

    def salary(self,payment):
        self.payment+=payment
    
    def getName(self):
        return self.name
    def getPayment(self):
        return self.payment