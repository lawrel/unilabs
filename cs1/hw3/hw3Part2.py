#Code asks for a type of lego, 2x4,2x2,2x1,1x1, and lists how many pieces it can build from a given list.
import hw3_util
import math
legos = hw3_util.read_legos('legos.txt')
typelego = input("What type of lego do you need? ==> ")
print(typelego)
if typelego != "2x4" and typelego != "2x2" and typelego != "2x1" and typelego != "1x1":
    print("\nIllegal lego")
else:
    if typelego == "2x4":
        n2x4 = legos.count('2x4')
        n2x2 = math.floor(legos.count('2x2')/2)
        n2x1 = math.floor(legos.count('2x1')/4)
        n1x1 = math.floor(legos.count('1x1')/8)
        n = n1x1+n2x1+n2x4+n2x2
    elif typelego == "2x2":
        n2x4 = 0
        n2x2 = legos.count('2x2')
        n2x1 = math.floor(legos.count('2x1')/2)
        n1x1 = math.floor(legos.count('1x1')/4)
        n = n1x1+n2x1+n2x4+n2x2
    elif typelego == "2x1":
        n2x4 = 0
        n2x2 = 0
        n2x1 = legos.count('2x1')
        n1x1 = math.floor(legos.count('1x1')/2)
        n = n1x1+n2x1+n2x4+n2x2
    else:
        n2x4 = 0
        n2x2 = 0
        n2x1 = 0
        n1x1 = legos.count('1x1')
        n = n1x1+n2x1+n2x4+n2x2
    print("\nI can make {0} {1} pieces:\n     {2} pieces of {1} using 2x4 pieces.\n     {3} pieces of {1} using 2x2 pieces.\n     {4} pieces of {1} using 2x1 pieces.\n     {5} pieces of {1} using 1x1 pieces.".format(n,typelego,n2x4,n2x2,n2x1,n1x1))