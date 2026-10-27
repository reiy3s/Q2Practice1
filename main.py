from pyscript import display, document

# tuple: immutable
# list: mutable, may be mixed ; convert using list(); .append() to add at end; .insert() add to specific index; NOT REPLACING VALUE, REPLACE INDEX / POSITION

# --------------------------------------------------------------------->>

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

sample_set = {"Mikmikk"}

display(type(sample_set)) # returns <class 'dict'> if no value in sample_set

# --------------------------------------------------------------------->>

#set operators

#union via | operator or a.union(b) method <<<<<< adds everything

a = {'soda', 'candy', 'chocolate', 'cookies'}
b = {'chocolate', 'burger', 'nuggets', 'cookies'}
c = {'shawarma', 'quesadilla', 'soda'}

display (a | b | c) # can also be (a.union(b,c))

#intersection via & or .intersection() method <<<<<< only gets similar values

display (a & b & c) # can also be (a.intersection(b,c))

#difference via - or .difference() method <<<<<< gets values in a that are not in b or c

display (a - b - c) # can also be (a.difference(b,c))

#symmetric difference via ^ or .symmetric_difference() method <<<<<< gets values that in both sets except the common values / unique values only

display (a ^ b ^ c) # can also be (a.symmetric_difference(b,c))

# --------------------------------------------------------------------->>

#set inclusions and superset relations

#SUBSET
#set_1 = {"fries", "burger"}
#set_2 = {"fries", "burger", "coke", "applepie"}

#display(set_1.issubset(set_2)) # returns True if set 1 is a subset of set 2
    # can be set 1 <= set 2
#set 1 is less than set 2 >> set 1 is a subset of set 2 >> output is true


#PROPER SUBSET
#set_1 = {"fries", "burger"}
#set_2 = {"fries", "burger", "coke", "applepie"}

#display(set_1 < set_2) # returns True if set 1 is a proper subset of set 2
# everything in set 1 is in set 2 but not everything in set 2 is in set 1 >> output is true

#set_1 = {"fries", "burger"}
#set_2 = {"fries", "burger", "coke", "applepie"}

#display(set_1 < set_2) # returns True since set 1 is a proper subset of set 2
# returns False if set 1 is equal to set 2 (set 2 must be set 1 and MORE)


#SUPERSET
#set_1 = {"fries", "burger"}
#set_2 = {"fries", "burger", "coke", "applepie"}

#display(set_2.issuperset(set_1)) # returns True if set 1 is a superset of set 2
# can be set 1 >= set 2
#set 1 is NOT a superset of set 2 >> output is False


#PROPER SUPER SET
set_1 = {"fries", "burger"}
set_2 = {"fries", "burger", "coke", "applepie"}

display(set_2 > set_1) # returns True if set 2 is a proper superset of set 1
# everything in set 1 is in set 2 but not everything in set 2 is in set 1 >> output is true



#BASICALLY
# SUBSET = everything in a is in b
# PROPER SUBSET = everything in a is in b, b has more
# SUPERSET = everything in b is in a
# PROPER SUPERSET = everything in b is in a, b has more

# --------------------------------------------------------------------->>

#FROZEN SETS >> frozenset()

subjs = ["Math", "Science", "Filipino", "ICT"]
convert_subjs = frozenset(subjs) # converts list to frozenset, immutable sets

display(convert_subjs)

# --------------------------------------------------------------------->>

#DICTIONARIES