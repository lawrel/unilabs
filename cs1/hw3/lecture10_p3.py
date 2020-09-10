co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
above_avg = 0
avg = round(sum(co2_levels)/len(co2_levels),2)
for i in co2_levels:
    if i > avg:
        above_avg += 1
print("Average:",avg)
print("Num above average:",above_avg)