'''
Read input.
Store in arrays.
for each transaction:
    create object


'''

'''
CSV FORMAT

Starting with row #2.

A,B,C,D,E,F...
A: Quantity of BTC purchased/sold
B: Price in USD
C: Fee (Amount paid to the Exchange company)
D: Other fee (e.g. bank fee) (Enter 0 if none.)
E: Datetime (Format TBD)
F,G,...: Optional other details (e.g. which exchange used, other comment)
'''

import csv
import math

# Validation??

'''
# round to 8 decimal places
def round(num):
    return math.ceil(num*100000000)/100000000
'''

# transaction class
class Transaction:
    def __init__(self,q,p,f,of):
        self.quantity = round(float(q),8) #BTC
        self.price = float(p) # USD per BTC
        self.fee = float(f) # in USD
        self.otherFee = of # For example, bank transfer fee. Not part of cost basis. (in USD)
        # self.date = d

    def getQuant(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getFee(self):
        return self.fee    

transactions = []

# holding class
# properties: quantity, cost, date
class Holding:
    def __init__(self,q,b,bwf):
        # self.id = ???
        self.quantity = q
        self.basis = b
        self.basisWithFees = bwf

holdings_fifo = []
holdings_lifo = []
holdings_avg = []

# METHODS

# Read
def read():
    ifile  = open('sample-transactions.csv', "rU")
    reader = csv.reader(ifile)

    for row in reader:
        quantity = row[0]
        price = row[1]
        commission = row[2]
        fee = row[3]
        t = Transaction(quantity,price,commission,fee)
        transactions.append(t)


# Add
def addToHoldings(t):
    quantity = t.getQuant()
    price = t.getPrice()
    fee = t.getFee()
    priceWithFeesPerUnit = round(((price*quantity) + fee) / qunatity, 8)
    h = Holding(quantity,price,priceWithFeesPerUnit)
    holdings_fifo.append(h)
    holdings_lifo.append(h)
    # add to average

# Remove
def removeFromHoldings(t):
    pass

# Write
# write (starting and) final holdings
# write gain or loss

# report



# EXECUTION

# LOAD TRANSACTIONS
read()

# PROCESS TRANSACTIONS
total_holdings = 0

for i in transactions:
    quantity = i.getQuant()
    total_holdings += quantity # Update holdings
    if quantity > 0:
        addToHoldings(i)
    else:
        removeFromHoldings(i)

#troubleshooting
index = 1

for t in transactions:
    print str(index) + ": Quantity: " + str(t.quantity) + "\n"
    index += 1

print "Current holdings: " + str(total_holdings) + " BTC. If this does not match your current holdings, there is a transaction missing."
