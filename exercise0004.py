from math import tan, pi

nsides = int(input('Input number of sides: '))
sLength = float(input('Input the length of a side: '))

pArea = nsides * (sLength ** 2) / (4 * tan(pi / nsides))

print(f'The area of the polygon is: {pArea}')