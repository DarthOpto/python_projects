"""
Calculate Compound interest
Equation
A = P(1+r)t

A = Money at the End
P = Principal/Original Amount Invested
r = Interest Rate
t = Years or Time Periods the money has been invested.
"""
import matplotlib.pyplot as plt


def compound_interest(p, r, t):
    """
    Calculate Compound Interest
    :param p: Principal investment
    :param r: interest rate
    :param t: years or time periods
    :return: Money at the end
    """
    a = p * (1 + r) ** t
    return a


def create_array(p, r, t):
    values = [p]
    years = [0]
    for time in range(1, t + 1):
        values.append(compound_interest(p, r, time))
        years.append(time)
    return values, years

values, years = create_array(100, .02, 25)
plt.plot(years, values, 'r')
values, years = create_array(100, .07, 25)
plt.plot(years, values, 'g')
values, years = create_array(100, .14, 25)
plt.plot(years, values, 'b')
plt.show()


