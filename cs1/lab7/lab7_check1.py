def parse_line(line):
    if line.count("/") >= 3:
        splitline = line.rsplit('/',3)
        for i in range(-3,0):
            if not (splitline[i].isdigit()):
                return None
        return(int(splitline[1]),int(splitline[2]),int(splitline[3]),splitline[0])
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line("    Here is some spaces 12/32/4"))
print(parse_line(" Again some spaces\n/12/12/12"))