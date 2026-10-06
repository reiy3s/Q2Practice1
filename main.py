# tuple: immutable
# list: mutable, may be mixed ; convert using list(); .append() to add at end; .insert() add to specific index; NOT REPLACING VALUE, REPLACE INDEX / POSITION

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
del days[3] # delete by index, deletes Thursday
print(days)