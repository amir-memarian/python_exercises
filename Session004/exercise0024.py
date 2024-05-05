from numpy import zeros # python -m pip install numpy
# import numpy as np

def rotate(a,n):
    b = zeros((n,n))
    for i in range(0, n):
        for j in range(0, n):
            b[j, n - 1 - i] = a[i , j]
    return b

def read(a, n):
    for i in range(0, n):
        print(f"Enter {n} numbers for row {i + 1}",end =" :")
        s = input().split(' ')
        for j in range(0, n):
            a[i, j] = int(s[j])

def print1(a, n):
    for i in range(0, n):
        for j in range(0, n):
            print(f"  {a[i,j]}",end='')
        print()

def main():
    n = int(input("Enter n: "))
    num = zeros((n,n))
    read(num, n)
    print("Primary array is ")
    print1(num, n)
    num = rotate(num, n)
    print("Rotated array is")
    print1(num, n)

main()