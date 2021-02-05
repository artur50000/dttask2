import json

# task n2. create function to calculate the amount of cumulative loan interests


def int_calc(principal, rate, year_period):
    principal = int(principal[:-3])
    rate = int(rate)
    year_period = int(year_period)
    total = principal * ((1 + rate / 100)**year_period)
    int_sum = total - principal
    return int_sum


with open('data.json') as f:
    message = json.load(f)


for key, value in message.items():
    int_customer = int(
        int_calc(
            value['principal'],
            value['rate'],
            value['year period']))
    print(f"interests calculation for the {key} is {int_customer} USD")
