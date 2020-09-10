#problem 1
def compare_date(date1,date2):
    if date1 == date2:
        return 0
    elif date1[1] == date2[1] and date1[0] < date2[0]:
        return -1
    elif date1[1] < date2[1]:
        return -1
    return 1
print(compare_date( [10,1995], [8,1995] ))
print(compare_date( [5,2010], [5,2010] ))
print(compare_date( [10,1993], [8,1998] ))
#problem 2
v = [ 7, 3, 1, 5, 10, 6 ]
v.sort()
print("{} {}".format(v[-2],v[-1]))
#problem 3
restaurants = [ [ 'Acme', 'Italian', 2, 4, 3, 5],[ 'Flintstone', 'Steak', 5, 2, 4, 3, 3, 4],[ 'Bella Troy', 'Italian', 1, 4, 5] ]
for i in range(len(restaurants)):
    if restaurants[i][1] == 'Italian':
        if 1 in restaurants[i] or 5 not in restaurants[i]:
            break
        else:
            print(restaurants[i][0])
#problem 4
"""def parse_line(line):
    parsed = line.split("|")
    return parsed
in_file = open('C:/Users/lawrem4/Dropbox/cs1/week6/yelp.txt')
for line in in_file:
    p_line = parse_line(line)
    print(p_line)"""
#problem 5
def chess_score(pieces):
    pawns = pieces.count("P")
    bishop = pieces.count("B")*3
    knight = pieces.count("K")*3
    rook = pieces.count("R")*5
    queen = pieces.count("Q")*9
    return pawns+bishop+queen+knight+rook
print(chess_score("BPQB"))
#problem 6
sumfirst = 0
sumsecond = 0
sumthird = 0
f = ["2, 5,7","3, 6,   10","1, 2, -3","2, 4, 1"]
for i in range(len(f)):
    f[i]=f[i].split(",")
    for x in range(len(f[i])):
        f[i][x] = int(f[i][x].strip())
    sumfirst += f[i][0]
    sumsecond += f[i][1]
    sumthird += f[i][2]
print("{}, {}, {}".format(sumfirst,sumsecond,sumthird))
#problem 7
a = list(range(100,-1,-1))
b = list(range(55,-2,-2))
c = list(range(3,30,2))
d = list(range(-95,91,5))
#problem 8 
v = [10,12,3,-5,5,6]
i = 0
s = 0
while i < len(v):
    if v[i] < 0:
        break
    s += v[i]
    i += 1
print(s)
#problem 9
v = [17, -5, 15, -3, 12, -5, 0, 12, 22, -1]
positive = []
for i in range(len(v)):

if positive == []:
    print('None')
else:
    print(positive.sort()) 