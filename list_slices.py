#As we've said before, omitting both start and end makes a copy of the whole list:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

#del instruction is able to delete more than just a list's 
#element at once - it can delete slices too
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#Deleting all the elements at once is possible too
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)