read_file = input("Enter the scores file: ")
print(read_file)
write_file = input("Enter the output file: ")
print(write_file)

f = open(read_file)
s = f.read()
print(s)
