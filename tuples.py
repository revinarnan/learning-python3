name = input("Enter file:")
if len(name) < 1 :          #set the default input when press the enter button
    name = "mbox-short.txt"

handle = open(name)         #open file
counts = dict()             #create empty dictionary
for line in handle:         #looping in every single line in the file
    if not line.startswith("From "):        #search words that starts with From:
        continue
    line = line.split()         #split every word independently
    time = line[5]
    hours = time.split(":")
    hour = hours[0]
    for h in hours[:1]:       #looping word in the line
        counts[h] = counts.get(h, 0) + 1

for hrs, count in sorted(counts.items()):
    print(hrs, count)
