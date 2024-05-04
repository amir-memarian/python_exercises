# y = 31x - 17x + 5  
# not *

x = int(input('Enter x: ')) 

m = (x << 5) - x    # (2^5 = 32)
n = -((x << 4) + x) # (2^4 = 16)

y = m + n + 5
print(f'y = {y}')