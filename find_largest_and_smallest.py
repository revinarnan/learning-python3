largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : #if you enter done, then the loop is stoped
        break
    try:    #try except for avoid invalid user input
        inum = int(num) #convert string to integer
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = inum
    elif smallest is None:
        smallest = inum
    elif inum < smallest:   #to find smallest value
        smallest = inum
    elif inum > largest:    #to find largest value
        largest = inum
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)

#this code is used to submit chapter 5 assignment in coursera's python for everybody
