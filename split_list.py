fname = input("Enter file name: ")
if len(fname) < 1 :           #set the default input when press the enter button
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From:"):
        continue
    count += 1
    line = line.rstrip()
    line = line.split()
    print(line[1])

print("There were", count, "lines in the file with From as the first word")
