📚 Python Set Methods

🔹 #1 – add() 
Adds a single element to the set (if it’s not already there).

my_set.add(5)

🔹 #2 – clear() 
Removes all elements from the set — totally wipes it.

my_set.clear()
🔹 #3 – copy() 
Creates a shallow copy of the set.

new_set = my_set.copy()

🔹 #4 – difference() 
Returns elements present in the first set but not in another.

set1.difference(set2)

🔹 #5 – difference_update() 
Removes all elements found in another set from the original.

set1.difference_update(set2)

🔹 #6 – intersection() 
Returns a set of elements common to both sets.

set1.intersection(set2)

🔹 #7 – isdisjoint() 
Checks if two sets have no elements in common.

set1.isdisjoint(set2)

🔹 #8 – issuperset() 
Returns True if the current set contains all elements of another.

set1.issuperset(set2)

🔹 #9 – issubset() 

Returns True if the current set is fully contained in another.

set1.issubset(set2)

🔹 #10 – pop() 
Removes and returns a random element from the set.

my_set.pop()
