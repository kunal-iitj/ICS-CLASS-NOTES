# we are going to be studying list comprehension.
# list comprehension is another way of synthesising list

list = [1, 2, 3, 4] # this is the usual way of defining lists

# this is how we can use list comprehension
list1 = [x for x in list]
list2 = [x*2 for x in list]
list3 = [x + y for x in list for y in list]


# some examples of list comprehension
arr = ['smile' for x in list]  # here we are using list just to get the number of iterations
arr2 = ['smile' + str(x) for x in list]


alphabets = ['a', 'b', 'c']
combination = ['f' + a for a in alphabets] # this example is important for understanding powerset
print(combination)


# ----------------------------------------------------------------------------------

# power set is an application of list comprehension to some sorts
# power_set is a set of all the possible subsets of a particular string or list
# for example power_set of [1, 2] is [[], [1], [2], [1,2]]


# to solve this, we define a head element and make recrusive calls for finding the power set of the tail elements
# list = [1, 2, 3, 4] head: 1 and tail: [2, 3, 4]

def power_set(string):  # we could have also used a list
    # our first step is to define the power set of the tail
    sub_set = power_set(string[1:])  # this 1: is slicing the list

    return sub_set + [string[0] + x for x in sub_set]
    # here you are concatinating the head and the powerset of the tail
