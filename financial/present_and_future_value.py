"""
Return the present or future value of money with a set interest rate
"""


def future_or_present(future=False, principal=None, rate=None, time=None):
    discount = (1 + rate) ** time
    if future:
        future_value = principal * discount
        return future_value
    else:
        present_value = principal / discount
        return present_value

print(future_or_present(future=True, principal=100, rate=0.08, time=5))
print(future_or_present(principal=100, rate=0.08, time=5))