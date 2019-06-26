herolist = ["Chris Hemsworth", "Chris Pratt", "Tom Holland"]
sorry = "Unfortunately, RDJ cannot make the dinner."
message = ", you are invited to this special dinner."
print(sorry)
print("I have found a bigger table, so 3 more people are invited!")
herolist.insert(0, "Tom Hiddleston")
herolist.insert(1, "Mark Ruffalo")
herolist.append("Jeremy Renner")
for people in herolist:
    print(people + message)