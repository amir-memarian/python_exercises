import sys

str1 = "one"
str2 = "four"
str3 = "three"

print(f"Memory size of \'{str1}\' = {str(sys.getsizeof(str1))} bytes")
print(f"Memory size of \'{str2}\' = {str(sys.getsizeof(str2))} bytes")
print(f"Memory size of \'{str3}\' = {str(sys.getsizeof(str3))} bytes")