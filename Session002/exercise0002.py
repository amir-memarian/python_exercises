while True:
    num = int(input('Enter a number:'))
    sum = 0
    for i in range(1,num):
        if (num % i == 0):
            sum += i
    
    if (sum == num):
        print('\tPerfected')
    else:
        print('\t Not perfect')
    
    yes = input("Continue?")
    if (yes[0] == 'N' or yes[0] == 'n'):
        break
    
