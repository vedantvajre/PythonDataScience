print("Hi")
herolist = ["Chris Pratt", "Tom Holland", "RDJ"]
message = ", you are invited to a special dinner."
for people in herolist:
    print(people + message)
del herolist[2]
print(herolist)
herolist.insert(0, "Chris Hemsworth")


