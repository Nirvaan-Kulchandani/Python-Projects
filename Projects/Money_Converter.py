# pip install forex_python

import forex_python.converter

def convert_currency(amount, from_currency, to_currency):
    '''Convert currency using forex-python library.'''

    converter = forex_python.converter.CurrencyRates()

    try:
        converted_amount = converter.convert(from_currency, to_currency,amount)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

    except Exception:
        print("Error while converting currency.")

amount = int(input("Enter Amount: "))
convertfrom = input("Enter currency that will be converted: ").upper()
convert_to = input("Enter currency in which the amount will be converted: ").upper()

convert_currency(amount, convertfrom, convert_to)
    