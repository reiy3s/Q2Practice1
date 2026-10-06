from pyscript import display, document

# tuple: immutable
# list: mutable, may be mixed ; convert using list(); .append() to add at end; .insert() add to specific index; NOT REPLACING VALUE, REPLACE INDEX / POSITION

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#del days[3] # delete by index, deletes Thursday

#days.remove("Friday") # delete by value, deletes Friday

#days.pop(1) # delete by index (last if no index) <-- more flexible

#days.clear() # delete all values, only []

#print("Monday" in days) # check if value exists in list, returns True or False

#len(days) # returns length of list

#days.count("Monday") # counts how many times a value appears in list

#copy

#days.sort() # sorts list in alphabetical (strings) / numerical (numbers)

#days.reverse() # reverses list order

display (days)

# --------------------------------------------------------------------->>

yummies = ["Mango", "Banana", "Apple"]

#print("Mango" in yummies) # check if value exists in list, returns True or False

#len(yummies) # returns length of list

#yummies.count("Mango") # counts how many times a value appears in list

#copy

#yummies.sort() # sorts list in alphabetical (strings) / numerical (numbers)

#yummies.reverse() # reverses list order

display (yummies)

# --------------------------------------------------------------------->>

#method operates on data
#function returns / passes on the data

# --------------------------------------------------------------------->>

#sets: unordered elements, unique values / no dupes, mutable but elements are immutable (can insert tuples, str, float, etc)

dog = {"Alaskan Klee Kai", "American Eskimo Dog", "Beagle"}

dog.add("Japanese Spitz") # add new value to set

display(dog)

# --------------------------------------------------------------------->>

sample_set = {}

display(type(sample_set)) # returns <class 'dict'>, not set