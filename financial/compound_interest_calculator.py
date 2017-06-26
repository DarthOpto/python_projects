"""
Calculate Compound interest
Equation
A = P(1+r)t

A = Money at the End
P = Principal/Original Amount Invested
r = Interest Rate
t = Years or Time Periods the money has been invested.
"""
from decimal import Decimal


def compound_interest():
    print('\n Greetings, let\'s calculate some interest \n')
    principal = Decimal(input('Please enter your Original amount invested: \n'))
    rate = Decimal(input('Please enter the interest rate: \n'))
    time = int(input('Please enter the the amount of time your money will be invested: \n'))
    print('Thank you. Now calculating what your original investment of: {0}, would be at a rate'
          'of: {1} after {2} number of years'.format(principal, rate, time))
    money_at_end = Decimal(principal * (1 + rate) ** time)
    print(money_at_end)

compound_interest()
