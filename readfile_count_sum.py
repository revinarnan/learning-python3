# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    nline = line[19:].rstrip()
    fline = float(nline)
    x += fline
    #print(x)
print("Average spam confidence:", x/count)
