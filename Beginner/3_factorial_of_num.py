def factorial(x):
    if x == 1:
        return 1
    else:
        # Recursive call to the function
        return x * factorial(x - 1)

num = int(input("Enter the number you want factorial of: "))
print(factorial(num))