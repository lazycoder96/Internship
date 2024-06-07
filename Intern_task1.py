#Creating List , Set and Dictionary

List = [1,2,3,4,5]
Dictionary = {'Car': 50000, 'Bike':20000, 'Cycle' : 10000}
Set ={6,7,8,9,10}

#Print original values Before performing Operation
print("Original List = ",List)
print("\n Original Dictionary = ",Dictionary)
print("\n Original Set = ",Set)

#Perform Operations on List

#1.Adding element at last of the List
List.append(99)
print("\n List after adding element = ", List)

#2.Removing Element from the List
List.remove(3)
print("\n List after removing element = ", List)

#3.Modifying elements of the List
List[3] = 100
print("\n List after modifying element = ", List)

#Perform Operation on Dictionary

#1.Adding a key-value pair
Dictionary['Truck'] = 40000
print("\n Dictionary after adding a key-value pair : ", Dictionary)

#2.Deleting Data from Dictionary
del Dictionary['Cycle']
print("\n Dictionary after Deleting a key-value pair : ", Dictionary)

#3.Modifying the Data in Dictionary
Dictionary["Bike"] = 25000
print("\n Dictionary after Updating Data : ", Dictionary)


#Perform Operations on Set

#1.Remove Element
Set.remove(10)
print("\n Set after removing 10 : ", Set)

#2.Adding Element
Set.add(1000)
print("\n Set after adding 1000 :", Set)

#Printing final Outputs after operations

print("\n Final List : ", List)
print("\n Final Dictionary : ", Dictionary)
print("\n Final Set : ", Set)