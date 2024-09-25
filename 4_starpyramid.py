def pyramid(n):
    x = int(round((n*2)/2))
    for i in range(1,(n*2)+1,2):
        print(" "*x + "*"*(i))
        x=x-1

pyramid(21)#Produces n-1 rows of pyramid