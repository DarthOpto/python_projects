# Lesson 2: Calculating Tax learning functions

import decimal


def calculator(meal=0.00, tax_rate=0.00, tip_rate=0.00):
    """
    Calculate the meal total including tax, and tip
    :param meal: decimal value of the meal
    :param tax_rate: decimal value of the tax rate
    :param tip_rate: decimal value of the tip rate
    :return: decimal value of the total meal cost
    """
    tax = meal * tax_rate
    tip = (meal + tax) * tip_rate
    total = meal + tax + tip
    return(total)

calculator(100.00, .15, .15)


