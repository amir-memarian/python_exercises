def lastWord(s):
    words = s.split()
    if len(words) == 0:
        return ""
    return words[-1]

s = input("Enter a string: ")
print(f"Last word is : {lastWord(s)}")
