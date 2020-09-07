finput = input("Enter file name: ") #file must in the same folder

fhandle = open(finput) #count characters in file
fread = fhandle.read()
char = len(fread)

fhand = open(finput) #count lines in file
count = 0
for line in fhand:
    line = line.rstrip()
    print(line.upper()) #print file content with all char upper case
    count = count + 1

print("\n", count, "lines and", char, "characters.")
