from math import pow
# import math

v = float(input('Input wind speed in kilometers/hour: '))
t = float(input('Input air temperature in degrees celsius: '))

# wci = 13.12 + 0.6215*t - 11.37*math.pow(v,0.16) + 0.3965*t*math.pow(v,0.16)
wci = 13.12 + 0.6215*t - 11.37*pow(v,0.16) + 0.3965*t*pow(v,0.16)

print(f'The wind chill index is {int(round(wci,0))}')