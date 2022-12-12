# # loop in list
# my_list=[1,2,4,5,6,3,"hello",9,7,55,88]
# sum=0
# for element in my_list:
#     print(element)

# # add upto integer on list
# for element in my_list:
#     if type(element)==int:
#         sum=element+sum
#         print("sum:",sum)
# # index-here if empty then it goes upto last
# print(my_list[::2])

# # starting of index is 1
# print(my_list[1::3])

# # inside the box first it indicates starting second upto where you want and next is how difference you want 
# # lst=[initial:End:index jump]
# my_list1=my_list[0:-1:3]
# print(my_list1)

# #to print from opposite of list starting is in first, second is ending and third is difference if you write nothing in second it will go upto last of the list if written then  it goes upto last plus 1
# my_list2=my_list[-2::-3]
# print(my_list2)

# # we can write list inside list
# my_list=(("apple","hash"),my_list1)
# print(my_list)

# # In matix every bracket is index from 0 to -1 and inside bracket it is also index from 0to -1
# mat_a=[[1,2,3],[4,5,6],[7,8,9]]
# mat_b=[[10,11,12]]
# print(mat_a[1][-2])
# # append is used as addition in last
# mat_c=mat_a[0]+mat_b[0]
# print(mat_c)

X = [[1,8,4],
    [4 ,5,6],
    [5 ,8,9]]

Y = [[15,8,3],
    [6,4,7],
    [4,6,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
print(len(Y[0]))

for i in range(len(X)):
   
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print(result)
print(len(Y))
print(len(X))
for i in range(len(X)):
    for j in range(len(Y[0])):
        result[i][j]=0
        for k in range(len(Y)):
            result[i][j]=result[i][j]+X[i][k]*Y[k][j]
print(result)

