# Define exchange rates (as of a particular date)
exchange_rates = {
    'USD': 1.0,    # Base currency (USD)
    'EUR': 0.85,   # Exchange rate for 1 USD to EUR
    'GBP': 0.75,   # Exchange rate for 1 USD to GBP
    'JPY': 110.28, # Exchange rate for 1 USD to JPY
    # Add more currencies and their respective exchange rates as needed
}

def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not found in the exchange rates."

    # Convert the amount to the equivalent in USD first
    usd_amount = amount / exchange_rates[from_currency]
    
    # Convert the amount from USD to the target currency
    result = usd_amount * exchange_rates[to_currency]
    return result

# Take user input for amount and currencies
amount = float(input("Enter the amount: "))
from_currency = input("Convert from (e.g. USD): ").upper()
to_currency = input("Convert to (e.g. EUR): ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} equals {result} {to_currency}")
