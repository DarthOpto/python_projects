"""
Return the present or future value of money with a set interest rate
"""


def TVM(p, r, t, type):
    discount = (1 + r) ** t
    if type == "FV":
        A = p * discount
        return A
    if type == "PV":
        A = p / discount
        return A

payments = [100, 200, 300, 400]
years = [5, 10, 15, 20]
rates = [.01, .02, .03, .04]


def totalTVM(payments, years, rates):
    total = 0
    for index in range(0, len(payments)):
        total += TVM(payments[index], years[index], rates[index], "PV")
    return total



total = 0
for year in range(1, 1001):
    total += TVM(100, .02, year, "PV")
print(total)