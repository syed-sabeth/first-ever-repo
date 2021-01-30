## TUPLE BASICS
'''my_tuple = (23, 34, 56, 32, 67, 94, 56)
print(my_tuple[6])
print(32 in my_tuple)
new_tuple = my_tuple[2:7] ##slicing off tuples.
print(new_tuple)
x, y, z, *others = (23, 34, 56, 32, 67, 94, 56)
print(x)
print(y)
print(z)
print(others)
print(my_tuple.count(56))
print(my_tuple.index(67))
print(len(my_tuple))'''

## SETS BASICS

my_set = {23, 34, 56, 32, 67, 94, 56}
my_set.add(25)
my_set.add(34) ##not operable as there cannot be  any duplicates.
#print(my_set)
set_2 = {23, 43, 123, 67, 56, 42, 13, 5, 94, 7}
## simple way to eliminate duplicates from a list.
'''lst = [12, 34, 54, 67, 45, 34, 54, 213, 431, 145, 67, 213, 213, 12]
set1 = set(lst)
print(set1)
lst2  =list(set1)
lst2.sort()
print(lst2)
print(67 in set1)
print(234 in set1)'''
#print(set_2)
#print(my_set.difference(set_2))
#set_2.discard(43)## removes 43 from set_2
#my_set.difference_update(set_2)
#set_2.intersection(my_set)
#print(my_set)
#print(set_2)
'''set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {4, 5, 6, 7, 8, 9, 10, 11}
print(set1)
print(set2)
print(set1.intersection(set2))'''
print(set_2 | my_set) # union
print(my_set & set_2) ## intersection



