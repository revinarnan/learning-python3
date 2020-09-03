score = input("Input your score (0.0 - 1.0): ")
sc = float(score)

if 0.0 <= sc <= 1.0:
    if sc < 0.6:
        print("F")
    elif 0.6 <= sc < 0.7:
        print("D")
    elif 0.7 <= sc < 0.8:
        print("C")
    elif 0.8 <= sc < 0.9:
        print("B")
    elif 0.9 <= sc < 1.0:
        print("A")
else:
    print("Value out of range.")
