def parse_line(line):
    if line.count("/") >= 3:
        splitline = line.rsplit('/',3)
        for i in range(-3,0):
            if not (splitline[i].isdigit()):
                return None
        return(splitline[1],int(splitline[2]),int(splitline[3]),splitline[0])
def get_line(fname,parno,lineno):
    paragraph = 1
    linen = 0
    flist = []
    for line in open(fname):
        flist.append(line)
    for line in range(len(flist)-1):
        if flist[line] == "\n" and flist[line+1] != "\n":
            paragraph += 1
        if paragraph == parno:
            if linen != lineno:
                linen += 1
            elif linen == lineno:
                return flist[line]
            
fname = input("Please enter the file number ==> ")+".txt"
parno = int(input("Please enter the paragraph number ==> "))
lineno = int(input("Please enter the line number ==> "))
end = ""
f_out = open("program.py","w")
line = get_line(fname,parno,lineno).strip()
while line != "END/0/0/0":
    fname,parno,lineno,code = parse_line(line)
    fname = fname+".txt"
    f_out.write(code+"\n")
    end = get_line(fname,parno,lineno).strip()
    line = get_line(fname,parno,lineno).rstrip()
f_out.close()
import program.py
