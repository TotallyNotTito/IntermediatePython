myFaveFoods = ["Mac & Cheese", "Hot Dogs", "Mango", "Carrots"]
#print(myFaveFoods)

"""
for i in myFaveFoods :
    print(i, end=", ")
"""

mixedLists = [5, True, myFaveFoods]
#print(mixedLists[2][2])

for i in mixedLists :
    if myFaveFoods in mixedLists :
        print("yes")
        break #don't like putting breaks in loops\

if (len(myFaveFoods) >= len(mixedLists)) :
    print("myFaveFoods is at least as long as mixed list:", 
    len(myFaveFoods), " number of items")
    myFaveFoods.append("Burritos")
    mixedLists.insert(len(mixedLists),False)
    
else : 
    print("myFaveFoods is not as long as mixed list:", 
    len(mixedLists), " number of items")
    mixedLists.append(False)

print(myFaveFoods)
print(mixedLists)