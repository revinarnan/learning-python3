fname = input("Enter file name: ") #input file
fh = open(fname)
lst = list() #empty list

for line in fh:             #split per words
    line = line.rstrip()
    line = line.split()
    for nline in line:      #check if words exist in lst, if not then append
        if nline in lst:
            continue
        else:
            lst.append(nline)
lst.sort()          #sort list alphabetical order
print(lst)
