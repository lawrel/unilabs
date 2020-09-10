def earlier_semester(class1,class2):
    semester1,year1 = class1
    semester2,year2 = class2
    if year1 == year2 and semester1 == "Fall":
        return False
    elif year1 > year2:
        return False
    elif year1 == year2 and semester1 == semester2:
        return False
    return True
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w3,w2)))