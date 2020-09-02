hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

def computepay(h, r):
    if h <= 40:
        ro = 0
    elif h > 40:
        ro = r * 0.5 * (h - 40)
    pay = h * r + ro
    return print("Pay", pay)

computepay(h, r)
