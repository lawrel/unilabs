values = []
stop = False
while stop == False:
    x = int(input("Enter a value (0 to end): "))
    print(x)
    if x == 0:
        stop = True
    else:
        values.append(x)
minval = min(values)
maxval = max(values)
avg = round(sum(values)/len(values),1)
print("Min: {0}\nMax: {1}\nAvg: {2}".format(minval,maxval,avg))