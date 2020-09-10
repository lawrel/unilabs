filename = input("Enter the scores file: ")
print(filename)
filename2 = input("Enter the output file: ")
print(filename2)
for s in open(filename):
    
f_out = open(filename2,"w")