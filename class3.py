import functools

"""
    HomeTask for 29.08.19
"""

# A little repetition:

# You have an array a=[1,3,4,2,5,8,2], put 3 on the third place(remember from what number does indexing starts?)
# Append to the array received in the previous paragraph in the end 5 and 7
# Delete from the array received in the previous paragraph all 5s
# Sort the array received in the previous paragraph

a = [1, 3, 4, 2, 5, 8, 2]
a[2] = 3

a.append(5)
a.append(7)

a.remove(5)

a.sort(reverse=False)

print(a)

# Main course:

# Take a list
# a=[1,3,5,7,9,11,13,15,17,19]
# a=[0.1, 12, 34, 0.02, 10.5, 9.9999999999, 10.00000000000000000001, 7, 4]
# a=['a', 10, 13, '10', 'ten', 9, 9, 11, 11]
# and write a program that prints out all the elements of the list that are less than 10.

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
for element in a:
    if element < 10:
        print(element)

a = [0.1, 12, 34, 0.02, 10.5, 9.9999999999, 10.00000000000000000001, 7, 4]
for element in a:
    if element < 10.0:
        print(element)

a = ['a', 10, 13, '10', 'ten', 9, 9, 11, 11]

for element in a:
    if type(element) == 'Int':
        if element < 10:
            print(element)

# Write a program that takes a list
# a=[12, 13, 13, 14, 14.5, 17, 17]
# a=['1', 1, 0.1, 1, '01', '1', 10, '010', '10', [10, 20], [20, 10], 1, [10, 20], ['20', '10']]
# a=[-78, 60, -24, -77, 47, 20, 78, -73, 63, -56, 20, 89, 66, -44, 28, 64, 96, 60, 21, -42, 92, -7, -53, 42, -2, 37, -85, 32, -57, -35, -93, -30, -36, -78, 8, -47, -32, 28, 50, 44, -76, -63, 80, 47, 21, -90, 48, 9, -61, 26, -11, -89, 84, 4, -39, -82, -80, -27, -15, -8, 5, 62, -79, 19, 34, -30, 11, 72, 82, -72, -49, -75, -71, -31, 24, 36, -33, -1, -95, -78, -9, 96, 88, 82, 77, 93, -96, -52, 80, 77, 95, 57, -48, 14, -40, -81, -81, 97, 29, -27]
# and returns a new list that contains all the elements of the first list minus all the duplicates.

a = [12, 13, 13, 14, 14.5, 17, 17]
new_list = []
for elem in a:
    new_list.append(elem)
    a.remove(elem)
print new_list

a = ['1', 1, 0.1, 1, '01', '1', 10, '010', '10', [
    10, 20], [20, 10], 1, [10, 20], ['20', '10']]
new_list = []
for elem in a:
    new_list.append(elem)
    a.remove(elem)
print new_list

a = [-78, 60, -24, -77, 47, 20, 78, -73, 63, -56, 20, 89, 66, -44, 28, 64, 96, 60, 21, -42, 92, -7, -53, 42, -2, 37, -85, 32, -57, -35, -93, -30, -36, -78, 8, -47, -32, 28, 50, 44, -76, -63, 80, 47, 21, -90, 48, 9, -61,
     26, -11, -89, 84, 4, -39, -82, -80, -27, -15, -8, 5, 62, -79, 19, 34, -30, 11, 72, 82, -72, -49, -75, -71, -31, 24, 36, -33, -1, -95, -78, -9, 96, 88, 82, 77, 93, -96, -52, 80, 77, 95, 57, -48, 14, -40, -81, -81, 97, 29, -27]
new_list = []
for elem in a:
    new_list.append(elem)
    a.remove(elem)
print new_list


# Write a program that takes a string
# a="Special cases aren't special enough to break the rules."
# a="Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum in the Netherlands as a successor of a language called ABC. Guido remains Python's principal author, although it includes many contributions from others."
# 	and returns the same string, except with the words in backwards order.

a = "Special cases aren't special enough to break the rules."
my_list = a.split(' ')
my_reversed_string = ''
for elem in my_list:
    my_reversed_string = elem+' '+my_reversed_string
print (my_reversed_string)


a = "Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum in the Netherlands as a successor of a language called ABC. Guido remains Python's principal author, although it includes many contributions from others."
my_list = a.split(' ')
my_reversed_string = ''
for elem in my_list:
    my_reversed_string = elem+' '+my_reversed_string
print (my_reversed_string)
