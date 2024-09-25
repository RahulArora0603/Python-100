p = float(input("Enter the principal amount : "))

n = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

#calculate simple interest by using this formula
si = (p * n * r)/100
ci =  p * (pow((1 + r / 100), n)) - p

#print
print("Simple interest : {}".format(si))
#print
print("Compound interest : {}".format(ci))