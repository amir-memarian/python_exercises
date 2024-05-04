def leapYear(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
    
def main():
    y = int(input('Enter Year: '))
    print(f'Is a leap year ? {leapYear(y)}')

main()