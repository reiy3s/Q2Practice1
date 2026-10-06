# tuple: immutable
# list: mutable, may be mixed ; convert using list(); .append() to add at end; .insert() add to specific index; NOT REPLACING VALUE, REPLACE INDEX / POSITION

x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
del x[3] # delete by index, deletes Thursday
display(x)