# a program that reads in statistics for deaths and compares them
import hw4_util
import sys
trendline = ""
ca1 = input("Enter the first area to check => ")
print(ca1)
cdata1 = hw4_util.read_deaths(ca1)
if cdata1 == []:
    print(ca1,"is an invalid name")
    sys.exit()
ca2 = input("Enter the second area to check => ")
print(ca2)
cdata2 = hw4_util.read_deaths(ca2)
if cdata2 == []:
    print(ca2,"is an invalid name")
    sys.exit()
for i in range(0,11):
    dif = (cdata1[i]-cdata2[i])
    if dif > -51 and dif < 51:
        trendline += "="
    elif dif > 50:
        trendline += "-"
    elif dif < -50:
        trendline += "+"

print("\n       2013   2003\nTrend:",trendline[::-1]+"\n")
if trendline.count("+") == trendline.count("-"):
    print(ca1,"and",ca2,"are the same")
elif trendline.count("-") > trendline.count("+"):
    print("I would rather live in",ca2,"than",ca1)
else:
    print("I would rather live in",ca1,"than",ca2)