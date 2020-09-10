values = [ 14, 10, 8, 19, 7, 13 ]
int1 = int(input("Enter a value: "))
print(int1)
int2 = int(input("Enter another value: "))
print(int2)
values.append(int1)
values.insert(2,int2)
dif = max(values)-min(values)
avg = round(sum(values)/len(values),1)
print(values[3],values[-1])
values.sort()
med = (values[len(values)//2]+ values[(len(values)//2)-1])/2
print("Difference: {0}\nAverage: {1}\nMedian: {2}".format(dif,avg,med))