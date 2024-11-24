import sys
try:
    age = int(input("Enter your age : "))
except ValueError:
    print("Enter your age in numbers.")
    sys.exit(1)
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")                