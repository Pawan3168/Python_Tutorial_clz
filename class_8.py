# tuples cann't be modified 
tup=(1,55,'apple')
# print(tup[-1])
# for i in tup:
#     print(i)
# # list can be modified i.e can be remove and insert in list
# dumb=[1,5]
# dumb.insert(1,'apple') # inside the bracket first indicates the position where to insert the items
# print(dumb)

# dumb.append(4444) #it added at last of list
# print(dumb)


slang=list(tup) #conversion of tuples in list to add in tuple
print(slang)

slang.append('apple')
tup=tuple(slang) #conversion of list to tuples after change 
print(tup)
print(tup.count('apple')) #count the selected items inside the list

# Dictionary

classmate={'milan':'is good boy','Ishan':'is bad boy'}
for k, v in classmate.items(): #k for key and v for values and name the dictionary name and items must
    print(k,v)

print(classmate['Ishan']) #to search the value of key write dictionary name and put the key

mate="nalim"
for i in mate[::-1]:
    print(i)

