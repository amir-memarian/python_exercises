pi = 22 / 7
height = float(input('Height of cylinder: '))
radius = float(input('radius os cylinder: '))

volume = pi * radius * radius * height
surArea = ((2 * pi * radius) * height) + (2*(pi*(radius**2)))

print(f'Volume is: {volume}')
print(f'Surface Area is: {surArea}')