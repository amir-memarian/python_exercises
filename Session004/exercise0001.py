from array import *

def prim(a, tedad, num):
    for i in range(0, tedad):
        if num % a[i] == 0:
            return 0
    a.append(num)
    return 1

def main():
    tedad = 0
    p = array('i',[])
    n = int(input('Enter n: '))
    
    for i in range(2, n+1):
        if prim(p, tedad, i) == 1:
            tedad += 1
    
    print("Primary is ",end ='')
    
    for i in range(0,tedad):
        print(f"  {p[i]}",end = '')

main()
