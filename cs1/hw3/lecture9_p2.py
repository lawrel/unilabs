census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
avgs = 0
x = 0
while x < len(census)-1:
    avgs += round((census[x+1]-census[x])/census[x]*100,1)
    x += 1
avg = round(avgs/(len(census)-1),1)
print("Average = {0}%".format(avg))