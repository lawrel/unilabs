# a program that finds the bunny and fox populations for five years based on the populations this year
bpop = int(input("Number of bunnies ==> "))
fpop = int(input("Number of foxes ==> "))
def find_pop(bpop,fpop):
    bpop2 = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop2 = int(0.4 * fpop + 0.02 * fpop * bpop)
    bpop3 = int((10*bpop2)/(1+0.1*bpop2) - 0.05*bpop2*fpop2)
    fpop3 = int(0.4 * fpop2 + 0.02 * fpop2 * bpop2)
    bpop4 = int((10*bpop3)/(1+0.1*bpop3) - 0.05*bpop3*fpop3)
    fpop4 = int(0.4 * fpop3 + 0.02 * fpop3 * bpop3)  
    bpop5 = int((10*bpop4)/(1+0.1*bpop4) - 0.05*bpop4*fpop4)
    fpop5 = int(0.4 * fpop4 + 0.02 * fpop4 * bpop4)
    print("Year 1: {0} {1}\nYear 2: {2} {3}\nYear 3: {4} {5}\nYear 4: {6} {7}\nYear 5: {8} {9}".format(bpop,fpop,bpop2,fpop2,bpop3,fpop3,bpop4,fpop4,bpop5,fpop5))
find_pop(bpop,fpop)