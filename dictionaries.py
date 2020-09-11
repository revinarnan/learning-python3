name = input("Enter file:")
if len(name) < 1 :          #set the default input when press the enter button
    name = "mbox-short.txt"

handle = open(name)         #open file
counts = dict()             #create empty dictionary
for line in handle:         #looping in every single line in the file
    if not line.startswith("From:"):        #search words that starts with From:
        continue
    line = line.split()         #split every word independently
    new_line = line[1:2]        #split No.2 words in the list
    for word in new_line:       #looping word in the line
        counts[word] = counts.get(word, 0) + 1      #provide default value of zero when
                                                    #the key is not yet in the dictionary
                                                    #- then add one

bigcount = None
bigword = None
for word, count in counts.items():          #find the maximum number
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
