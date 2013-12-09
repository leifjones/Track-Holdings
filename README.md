Track-Holdings
==============

Objective
---------
Determine gain/loss by FIFO, LIFO, and Average methods

Context
-------
In the United States, an exchange of goods for USD is an event with tax concequences. As I understand it, an individual can choose to calculate gains and losses with regard to such exchange(s) of goods using one of three methods:
1) "first-in-first-out" (FIFO)
2) "last-in-first-out" (LIFO)
3) "average"

Calculating any of these by hand (or even with a spreadsheet) can be tedious. I have come across some attempts to automate this - but none that have clearly delineated outcomes for FIFO, LIFO, and average calculations.

Because I purchased and sold amounts of bitcoin this year (2013), I want a way to choose a calculation method and to accurately figure my gain. This is my attempt at creating a program to accomplish such.

BTC donations accepted: <address to be posted>

Goals: Track holdings of commodity/currency/stock/etc. to report gains/losses
Limitations: Not intended for exchange between multiple currencies

Outline of Program
------------------
1. Read transactions from CSV
2. Calculate holdings (according to FIFO/LIFO/average) after each transaction
3. Determin gain/loss
4. Output to TXT


Roadmap
-------
0.1: Read transaction data
     Create objects to represent holdings
     Track price of each holding
0.2: Allow for starting positions
0.3: Differentiate Long-Term and Short-term gains/losses
