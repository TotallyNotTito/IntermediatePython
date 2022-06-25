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
        break #don't like putting breaks in loops