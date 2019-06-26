herolist = ["Chris Hemsworth", "Tom Holland", "Chris Pratt", "Tom Hiddleston", "Mark Ruffalo", "Jeremy Renner"]
message = (", you are still invited to the dinner.")
print("Sadly our new dinner table won't arrive in time, and I will only be able to invite 2 people.")
herolist.pop(2)
print("Sorry Chris Pratt, I can't invite you to the dinner.")
herolist.pop(2)
print("Sorry Tom Hiddleston, I can't invite you to the dinner.")
herolist.pop(2)
print("Sorry Mark Ruffalo, I can't invite you to the dinner.")
herolist.pop(2)
print("Sorry Jeremy Renner, I can't invite you to the dinner.")
for people in herolist:
    print(people + message)



