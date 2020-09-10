hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)
if hs > he and hs > hd:
    print("Sam")
    if hd > he:
        print("Dale")
        print("Erin")
    elif he > hd:
        print("Erin")
        print("Dale")
elif hd > hs and hd > he:
    print("Dale")
    if hs > he:
        print("Sam")
        print("Erin")
    elif he > hs:
        print("Erin")
        print("Sam")
elif he > hs and he > hd:
    print("Erin")
    if hs > hd:
        print("Sam")
        print("Dale")
    elif hd > hs:
        print("Dale")
        print("Sam")