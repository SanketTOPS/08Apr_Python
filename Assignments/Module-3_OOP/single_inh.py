class father:
    bal=0
    car=0
    
    def getdata(self):
        self.bal=input("Enter bank balance details:")
        self.car=input("Enter car details:")

class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=son()
sn.getdata()
sn.printdata()