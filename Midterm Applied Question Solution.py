# Winter BUAN 346/446 Midterm Applied Question SOlutions
"""Currency Exchange Conversion"""

def currx(usd):
    """Move tortoise's position."""
    pound = usd * 0.84
    euro = usd * 0.95
    candollar = usd * 1.36
   
    return pound, euro, candollar

# run the race
input = int(input('Enter US dollar amount to convert: '))
output = currx(input)

print()
print('$',input,' is worth:',sep='')
print(output[0], 'British Pounds')
print(output[1], 'Euros')
print(output[2], 'Canadian Dollars')