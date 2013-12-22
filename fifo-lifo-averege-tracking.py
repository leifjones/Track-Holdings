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
D: Transfer costs (E.g. bank fee to include for your info) (Enter 0 if none.)
E: Datetime (Format TBD)
F,G,...: Optional other details (e.g. which exchange used, other comment)

In order for FIFO and LIFO to methods to be calculated currectly, transactions must be listed in the CSV by ascending order chronologoically.
(Oldest transactions first. Newest transactions last.
'''

import csv
import math

# Validation??


# round to X decimal places
def myRound(num,base):
    return float( round( num * (10**base) ) ) / (10**base)

# transaction class

# REWORK TO ALLOW FOR ALTERNATE CONSTRUCTOR - BASED ON AMT SPEND AND AMT RECEIVED (TO SIMPLIFY FEES ISSUES)
class Transaction:
    def __init__(self,q,p,f,xf):
        self.quantity = myRound(float(q),8) #BTC
        self.price = float(p) # USD per BTC
        self.fee = float(f) # in USD
        self.xfer = float(xf) # For example, bank transfer fee. Not part of cost basis. (in USD)
        # self.date = d
        # self.id = id # id number

    def __repr__(self):
        if self.quantity == 0:
            return "Empty transaction!"
        elif self.quantity > 0:
            return "Buy: {} BTC for a price of ${} per bitcoin.".format(str(self.quantity),str(self.price))
        else:
            return "Sale: {} BTC at price of ${} per bitcoin.".format(str(self.quantity),str(self.price))

    def getQuant(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getTotalFees(self):
        return self.fee +self.xfer

    

transactions = []

# holding class
# properties: quantity, cost, date
class Holding:
    def __init__(self,q,b,bwf):
        # self.id = ???
        self.quantity = myRound(float(q),8)
        self.basis = float(b) #per unit
        self.basisWithFees = float(bwf) # per unit

    def getQuant(self):
        return self.quantity
    def getBasis(self):
        return self.basis
    def getBWF(self):
        return self.basisWithFees

    def setQuant(self,newQuant):
        self.quantity = myRound(float(newQuant),8)

    def subtractX(self,toSubtract): # ONLY USE WHEN AMOUNT SUBTRACTING IS LESS THAN self.quantity
        self.quantity -= myRound(float(toSubtract),8)
        # Optionally include some validation

# AvgHolding class extends Holding class, adding weight

# INITIALIZE META-LISTS
holdings_fifo = [[],0] # [list of holdings], gain/loss
holdings_lifo = [[],0] # [list of holdings], gain/loss
holdings_avg = [[],0] # [list of holdings], gain/loss

# METHODS

# Read
def read():
    print "READING TRANSACTIONS FILE ..."
    ifile  = open('sample-transactions.csv', "rU")
    reader = csv.reader(ifile)

    print "GENERATING TRANSACTION list ..."
    for row in reader:
        quantity = row[0] # first collumn
        price = row[1] # 2nd collomn
        fee = row[2] # 3rd
        xfer = row[3] # 4th
        t = Transaction(quantity,price,fee,xfer)
        transactions.append(t)


# Add
def addToHoldings(t):
    quantity = t.getQuant()
    price = t.getPrice()
    totalFees = t.getTotalFees()
    priceWithFeesPerUnit = myRound(((price*quantity) + totalFees) / quantity, 8)
    h = Holding(quantity,price,priceWithFeesPerUnit)
    holdings_fifo[0].append(h)
    h = Holding(quantity,price,priceWithFeesPerUnit) # Re-initialize to append new object, rather than reference to original
    holdings_lifo[0].append(h)
    h = Holding(quantity,price,priceWithFeesPerUnit) # Re-initialize to append new object, rather than reference to original
    holdings_avg[0].append(h)

# Remove
def removeFromHoldings_fifo(t):
    quantity = -t.getQuant() # Negative sign because sales are entered as negative. Take postive value for local handling.
    price = t.getPrice()
    fees = t.getTotalFees()

    gainLoss = 0
    
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # Check if there are enough in first holding
            # if exactly enough, remove first holding & done w/ removing holdings
        holdingQuant = holdings_fifo[0][0].getQuant()
        holdingBasis = holdings_fifo[0][0].getBasis()
        if holdingQuant == quantity:
            print "Quantity matches amt in first holding. REMOVING & UPDATING GAIN/LOSS ..."
            print "{14.8f}".format(quantity*holdingBasis)
            print "{14.8f}".format(quantity*price)
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print "{14.8f}".format(gainLoss)
            holdings_fifo[0].pop(0)
            transactionFullyAccountedFor = True # Done with removing.
        elif quantity < holdingQuant:
            print "Quantity is smaller than amt in first holding. SUBTRACTING & UPDATING GAIN/LOSS..."
            print "Holding value was {}. SUBTRACTING {:.8f} ...".format(holdingQuant,quantity)
            print quantity*holdingBasis
            print quantity*price
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print gainLoss
            holdings_fifo[0][0].subtractX(quantity)
            print "Holding value is now {}.".format(str(holdings_fifo[0][0].getQuant()))
            transactionFullyAccountedFor = True # Done with removing.
        else: # Quantity sold exceeds value of the first remaining holding
            print "Quantity excedes amt in first holding. REMOVING and REPEATING ..."
            print quantity*holdingBasis
            print quantity*price
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print gainLoss
            quantity -= holdingQuant
            holdings_fifo[0].pop(0)
            # NOT done with removing. Continue.

    holdings_fifo[1] += myRound(gainLoss,8)

def removeFromHoldings_lifo(t):
    quantity = -t.getQuant() # Negative sign because sales are entered as negative. Take postive value for local handling.
    price = t.getPrice()
    fees = t.getTotalFees()

    gainLoss = 0
    
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # Check if there are enough in first holding
            # if exactly enough, remove first holding & done w/ removing holdings
        holdingQuant = holdings_lifo[0][-1].getQuant()
        holdingBasis = holdings_fifo[0][0].getBasis()
        if holdingQuant == quantity:
            print "Quantity matches amt in last holding. REMOVING ..."
            print (quantity*holdingBasis)
            print (quantity*price)
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print format(gainLoss)
            holdings_lifo[0].pop(-1)
            transactionFullyAccountedFor = True # Done with removing.
        elif quantity < holdingQuant:
            print "Quantity is smaller than amt in last holding. SUBTRACTING ..."
            print "Holding value was {}. SUBTRACTING {:.8f} ...".format(holdingQuant,quantity)
            print (quantity*holdingBasis)
            print (quantity*price)
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print (gainLoss)
            holdings_lifo[0][-1].subtractX(quantity)
            print "Holding value is now {}.".format(str(holdings_lifo[0][-1].getQuant()))
            transactionFullyAccountedFor = True # Done with removing.
        else: # Quantity sold exceeds value of the first remaining holding
            print "Quantity excedes amt in last holding. REMOVING and REPEATING ..."
            print (quantity*holdingBasis)
            print (quantity*price)
            gainLoss += myRound(quantity*price - quantity*holdingBasis,8)
            print (gainLoss)
            quantity -= holdingQuant
            holdings_lifo[0].pop(-1)
            # NOT done with removing. Continue.

    holdings_lifo[1] += myRound(gainLoss,8)

def removeFromHoldings_avg(t):
    quantity = -t.getQuant() # Negative sign because sales are entered as negative. Take postive value for local handling.
    price = t.getPrice()
    fees = t.getTotalFees()

    gainLoss = 0

    # assign proportional portions of the transaction to each holding:
    
    # update holdings
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # for each AvgHolding in list:
            # multiply(each.getWeight(), quantity)
            # subtract that value from the AvgHolding.quantity
            # ????? to update price
            # subtract quant from leftToProcess variable
        #check whether leftToProcess variable = 0. if not, error
        transactionFullyAccountedFor = True

    holdings_avg[1] += myRound(gainLoss,8)

# Calculate gain/loss

# known error
# 1: Ran out of holdings to complete transaction (report line # from CSV). Suggestion: Is there an un accounted for donation?

# Write
# write (starting and) final holdings
# write gain or loss

# report
def printHoldings(list): # Pass in list of holdings.
    i = 1
    for holding in list:
        print "{0}. Number of units: {1:14.8f} BTC.  Basis cost: {2:10.2f} USD per BTC".format(i,holding.getQuant(),holding.getBasis())
        # Increase the "14" if scaling to larger 4 figure holdings.
        i += 1


# EXECUTION

# LOAD TRANSACTIONS
read()

# PROCESS TRANSACTIONS
total_holdings = 0

transactionNum = 1
for i in transactions:
    print "PROCESSING TRANSACTION #{} ...".format(str(transactionNum))
    print i
    quantity = i.getQuant()
    total_holdings += quantity # Update holdings
    if quantity > 0:
        print "Transaction #{} is a buy. ADDING TO HOLDINGS ...".format(str(transactionNum))
        addToHoldings(i)
    else:
        print "Transaction #{} is a sell. SUBTRACTING FROM HOLDINGS ...".format(str(transactionNum))
        print "Starting rfh-FIFO..."
        removeFromHoldings_fifo(i)
        print "\nStarting rfh-LIFO..."
        removeFromHoldings_lifo(i)
        print "\nStarting rfh-AVG..."
        removeFromHoldings_avg(i)
    
    print "FIFO"
    printHoldings(holdings_fifo[0])
    # Calculate and print gain/loss
    print "LIFO"
    printHoldings(holdings_lifo[0])
    # Calculate and print gain/loss
    print "Average"
    printHoldings(holdings_avg[0])
    # Calculate and print gain/loss

    transactionNum += 1
    
    # Update gain/loss without fees
    # Update gain/loss with fees

print "Current holdings: " + str(total_holdings) + " BTC. If this does not match your current holdings, there is a transaction missing."

# Print or write gain/loss
print "FIFO Gain/Loss: ${}".format(holdings_fifo[1])
print "LIFO Gain/Loss: ${}".format(holdings_lifo[1])
print "Average Gain/Loss: ${}".format(holdings_avg[1])

#troubleshooting
index = 1

for t in transactions:
    print str(index) + ": Quantity: " + str(t.quantity) + "\n"
    index += 1


# print holdings_fifo[1].getBasis()
