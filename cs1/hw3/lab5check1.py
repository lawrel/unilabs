import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(restaurant,index):
    avg = sum(restaurant[index][6])/len(restaurant[index][6])
    x,y = restaurant[index][3].split("+")
    print("{0} ({1})".format(restaurant[index][0],restaurant[index][5]))
    print("\t{0}\n\t{1}".format(x,y))
    print("Average Score: {0:.2f}".format(avg))
print_info(restaurants,0)
print_info(restaurants,4)