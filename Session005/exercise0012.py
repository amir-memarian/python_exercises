s = input("Enter a string: ")
wordsIns = s.split()
result = ""
for word in wordsIns:
    result += word[0].upper() + word[1:].lower() + " "
print(result)