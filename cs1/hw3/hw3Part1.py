# Code asks for a year, a female and male name, and finds data about those names in a range +- 10 years from the given
import read_names
import sys
#function to check that a name/any names are on the list for the given year, then prints info if all is valid
def check(names,counts,year,name):
    if names == []:
        pass
    elif names.count(name) == 0:
        print("   {0}: Not in the top 250".format(year))
    else:
        rank = (names.index(name)+1)
        count = counts[names.index(name)]
        percenttop = count/counts[0]*100
        percentall = count/sum(counts)*100
        print("   {0}: {1:3d} {2:5d} {3:7.3f} {4:7.3f}".format(year,rank,count,percenttop,percentall))
#functions for finding data on female and male names for the range of years
def femname():
    name = input("Enter a female name => ")
    print(name)
    (names,counts) = read_names.top_in_year(year, 'f')
    (names5,counts5) = read_names.top_in_year(year+5, 'f')
    (names10,counts10) = read_names.top_in_year(year+10, 'f')
    (names_5,counts_5) = read_names.top_in_year(year-5, 'f')
    (names_10,counts_10) = read_names.top_in_year(year-10, 'f')
    print("Data about female names\n"+name+":")
    check(names_10,counts_10,year-10,name)
    check(names_5,counts_5,year-5,name)
    check(names,counts,year,name)
    check(names5,counts5,year+5,name)
    check(names10,counts10,year+10,name)
def malename():
    name = input("Enter a male name => ")
    print(name)
    print("Data about male names\n"+name+":")
    (names,counts) = read_names.top_in_year(year, 'M')
    (names5,counts5) = read_names.top_in_year(year+5, 'M')
    (names10,counts10) = read_names.top_in_year(year+10, 'M')
    (names_5,counts_5) = read_names.top_in_year(year-5, 'M')
    (names_10,counts_10) = read_names.top_in_year(year-10, 'M')
    check(names_10,counts_10,year-10,name)
    check(names_5,counts_5,year-5,name)
    check(names,counts,year,name)
    check(names5,counts5,year+5,name)
    check(names10,counts10,year+10,name)
read_names.read_from_file("top_names_1880_to_2014.txt")
year = int(input("Enter the year to check => "))
print(year)
if 1880 > year or year > 2014:
    print("Year must be at least 1880 and at most 2014")
    sys.exit()
femname()
print("")
malename()