# Yuria Loo
# IT 111
# 2024-04-03
# Practice in Class 1: Purchase Receipt

# declares a constant variable for the tax rate
TAX_RATE = 0.1

# asks an user for their name and the amount of thier purchased bill
name   = input('Enter your name?')
amount = float(input('Enter the amount of your purchase: '))

taxCalc = amount * TAX_RATE
total   = amount + taxCalc

# displays the result
print()
print('Hello ', name + ', here is your sales receipt:')
print('Subtotal = $', format(amount,     '8,.2f'))
print('     Tax = $', format(taxCalc,    '8,.2f'))
print('            ', format('--------', '8s'))
print('   Total = $', format(total,      '8,.2f'))
