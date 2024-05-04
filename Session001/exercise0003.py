from math import pi

# pi = 22 / 7

radius = float(input('Radius of sphere: '))

surArea = 4 * pi * (radius ** 2)
volume = (4/3) * (pi * (radius ** 3))

print(f'surface Area is: {surArea}')
print(f'volume is: {volume}')