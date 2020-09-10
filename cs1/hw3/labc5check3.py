import lab05_util
import webbrowser
def print_info(restaurant,index):
    x,y = restaurant[index][3].split("+")
    print("{0} ({1})".format(restaurant[index][0],restaurant[index][5]))
    print("\t{0}\n\t{1}".format(x,y))
    if len(restaurant[index][6])>3:
        restaurant[index][6].sort()
        avg = (sum(restaurant[index][6])-min(restaurant[index][6])-max(restaurant[index][6]))/(len(restaurant[index][6])-2)
        length = len(restaurant[index][6])-2
    else:
        avg = sum(restaurant[index][6])/len(restaurant[index][6])
        length = len(restaurant[index][6])
    if avg <= 2:
        print("This restaurant is rated bad, based on {0} reviews.".format(length))
    elif avg > 2 and avg <= 3:
        print("This restaurant is rated average, based on {0} reviews.".format(length))
    elif avg > 3 and avg <= 4:
        print("This restaurant is rated above average, based on {0} reviews.".format(length))
    else:
        print("This restaurant is rated very good, based on {0} reviews.".format(length))
restaurants = lab05_util.read_yelp('yelp.txt')
index = int(input("Enter an ID number => "))-1
if index >= 0 and index <= len(restaurants)-1:
    print_info(restaurants,index)
else:
    print("That is not a valid id number.")
choice = input("""What would you like to do next?
    1. Visit the homepage
    2. Show on Google Maps
    3. Show directions to this restaurant
    Your choice (1-3)? ==> """)
if choice == "1":
    webbrowser.open(restaurants[index][4])
elif choice == "2":
    webbrowser.open("http://www.google.com/maps/place/{0}".format(restaurants[index][3]))
elif choice == "3":
    webbrowser.open("http://www.google.com/maps/dir/110 8th Street Troy NY/{0}".format(restaurants[index][3]))
else:
    print("That is not a valid entry.")