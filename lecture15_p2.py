filename = input("Data file name: ")
print(filename)
prefix = input("Prefix: ")
print(prefix)
names = set()
total = 0
for line in open(filename, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    lastname = words[0].strip().split(",")
    lastname[0].strip()
    if lastname[0] not in names:
        names.add(lastname[0].strip())
        if lastname[0][0:len(prefix):]== prefix:
            total += 1
print("{} last names".format(len(names)))
print("{} start with {}".format(total,prefix))