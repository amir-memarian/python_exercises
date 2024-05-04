amt = int(input('Enter amount: '))
rate = float(input('Enter rate: '))
years = int(input('Enter year: '))

future_value = amt * ((1+(0.01 * rate)) ** years)

print("Future value is %0.12f" % (future_value))