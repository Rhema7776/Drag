# collection
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# LISTS[]
fruits = ["apples", "strawberry",1, "oranges",4, "apples"]
print(type(fruits))

# To loop through a list

for x in fruits:
    print(x)

for x in range(len(fruits)):
    print(fruits[x])


# TUPLES()
tup1 = ("apples",1, "strawberry",True,1, "oranges")


# print(type(tup1))

# conv = list(tup1)
# # trying a list method

# conv.remove(1)
# print(conv)

# conv.insert(1, 'banana')
# print(conv)

# conv.append("melon")
# print(conv)

# conv.remove('oranges')
# print(conv)

# conv.pop(4)
# print(conv)

# ## OR
# # del conv[4]
# # print(conv)

# ## To completely delete a LIST,
# # del conv
# # print(conv)

# ANOTHER TUPLE
for x in range(0,10): #start, stop, step
    print(x)
# # DICTIONARIES{}
# Cars = {
#     "name": "mercedes",
#     "color": "grey",
#     "year" : "2000"
# }
# print(type(Cars))
# # SETS{}
# set1 = {"apples", "strawberry", "oranges"}
# print(type(set1))