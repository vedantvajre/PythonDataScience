herolist = ["Chris Pratt", "Tom Holland", "RDJ"]
del herolist[2]
herolist.insert(0, "Chris Hemsworth")
print(herolist)
sorry = "Unfortunately, RDJ cannot make the dinner."
message = ", you are invited to this special dinner."
print(sorry)
for people in herolist:
    print(people + message)