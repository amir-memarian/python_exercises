def reverse(n):
    if (n == 0):
        return
    else:
        print(f" {n}", end=' ')
        n = n - 1
        reverse(n)

def main():
    n = int(input('Enter n:'))
    print(end= "Result is ")
    reverse(n)

main()