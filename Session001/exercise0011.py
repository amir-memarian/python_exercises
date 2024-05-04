y1 = int(input('Enter price for first year: '))
y2 = int(input('Enter price for second year: '))

t = (float)(y2-y1) / y1
y3 = y1 + (y2 * t)

print(f'Extera=%{t}\t\tprice next year = {y3}')