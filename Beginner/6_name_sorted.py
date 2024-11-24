print("****           IF YOUR NAME WAS SORTED          ****\n")
name = input("Enter your name: ")
if name.replace(" ","").isalpha():
    res = ''.join(sorted(name.lower()))
    print(str(res))
else:
    raise ValueError("Enter your alphanumeric name.")

