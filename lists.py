myFaveFoods = ["Mac & Cheese", "Hot Dogs", "Mango", "Carrots"]
#print(myFaveFoods)

"""
for i in myFaveFoods :
    print(i, end=", ")

"""
mixed_lists = [5, True, myFaveFoods, False, "Lemon"]
#print(mixedLists[2][2])
"""
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

#print(myFaveFoods)
#print(mixedLists)

#mixedLists.pop()
# mixedLists.push("New Thing")
#.append("") is method of pushing items in to list
#print(mixedLists)

new_list = myFaveFoods + mixedLists
print("original mixe list: ",mixedLists)
print("sliced list: ",mixedLists[1:3])
print("step list: ", mixedLists[::2])
"""

#demonstrating shared memory
#new_list = mixed_lists
"""
methods for copying memory
- .copy()
- list(list_variable)
- list_variable[:]
"""

#new_list = mixed_lists.copy()
#new_list = list(mixed_lists)
"""
new_list = mixed_lists[:]
new_list.append("Not Sharing memory")
print("mixed_list items: ",mixed_lists)
print("new_list items: ", new_list)
"""

#LIST COMPREHENSION
list_ints = []
for i in range(10) :
    list_ints.append(i)

change_list = list_ints[i + 3 for i in list_ints]