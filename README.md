Track-Holdings Alpha (Pre-0.1)
==============================

#### DISCLAIMER
_While I make every effort to provide an quality script, I make no assurances. Under *no circumstances* does this tool serve as a substitute for the professional advice of an accountant and your own research, calculations, and decision-making. By using this tool, you claim all responsibility for the results of choices made after using this tool._

Primary Objective
-----------------
Determine gain/loss by FIFO, LIFO, and Average methods associated with exchanges between bitcoin and US dollars.

Scope
-----
This will be most applicable to the situation of someone who buys and sells bitcoin as a commodity. If you are holding and spending BTC, this tool _might_ be applicable if you figure the fair market value at the time of spending.

*Function*: Use this tool to figure gain/loss via the FIFO, LIFO, and average methods. Technically this tool can be used/modified for tracking any sort of holding (commodity, currency, bullion, stock, alpaca socks, etc.). Similarly, any base currency can be used instead of USD.

*Limitation*: This is not currently designed to process exchange between multiple digital currencies or multiply fiat currencies.

Further Context
---------------
I am the child of an certified public accountant. I worked as a tax preparer for a tax-prep franchise in the United States. Beyond these experiences, I have had no formal financial training; see disclaimer above.

In the United States, an exchange of goods for USD is an event with tax concequences. As I understand it, an individual can choose to calculate gains and losses with regard to such exchange(s) of goods using one of three methods:
1. "first-in-first-out" (FIFO)
2. "last-in-first-out" (LIFO)
3. "average"

Calculating any of these by hand (or even with a spreadsheet) can be quite tedious. If your number of transactions is greater than a dozen, software proves necessary. I have come across some attempts to automate this - but none that have clearly delineated outcomes for FIFO, LIFO, and average calculations. This is my attempt to make what I'm looking for ... and learn som Python at the same time!!

Because I purchased and sold amounts of bitcoin this year (2013), I want a way to choose a calculation method and to accurately figure my gain/loss. This is my attempt at creating a program to accomplish such.

BTC donations accepted: 1A6ujnfh6B3y82DzjWrs2vcpcFPFF13We6

Goals: Track holdings of commodity/currency/stock/etc. to report gains/losses
Limitations: Not intended for exchange between multiple currencies

Current Outline of Program
--------------------------
1. Read transactions from CSV
2. Calculate holdings (according to FIFO/LIFO/average) after each transaction
3. Determin gain/loss
4. Output to TXT(?)

Roadmap
-------
0.1
* Read transaction data
* Create objects to represent holdings
* Track price of each holding

0.2
* Allow for starting positions
* Report amount that this adds to tax owed to IRS based on tax bracket

0.3
* Differentiate Long-Term and Short-term gains/losses

0.4
* Explicit function to project gain/loss implications of a transaction

1.0
<ul>
  <li>Standalone format. Options being considered:
    <ul>
      <li>Webapp
        <ul>
          <li>Pros:
            <ul>
              <li>Google Spreadsheet integration via Google Apps Script</li>
              <li>In-browser, accessible anywhere, on any device</li>
            </ul>
          </li>
        </ul>
      </li>
      <li>Java
        <ul>
          <li>Pros:
            <ul>
              <li>Works on any desktop OS</li>
              <li>Internet connection not necessary</li>
            </ul>
          </li>
          <li>Cons:
            <ul>
              <li>If Steve Jobs's is right (or if his opinion wins out), Java's relevancy will diminish over time.</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
</ul>



Copyright 2013 Leif Segen. BTC donations are accepted: 1A6ujnfh6B3y82DzjWrs2vcpcFPFF13We6

This file is part of Track-Holdings.

Track-Holdings is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

Track-Holdings is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Track-Holdings.  If not, see <http://www.gnu.org/licenses/>.
