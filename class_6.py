# # # string
# my_string="Hello world from python"
# for i in my_string:
#     if i=="o":
#        i= i.upper()
#     print(i)

# # for formating of string to print we hve to use f infromt of string
# a=f"it's been a while!!"
# print(a)

# m="python"
# n="mero name {0} ho {1} ".format(m,my_string)
# # o ra 1 is the position inside format in 0 m is written and in 1 my_string is written
# print(n)

# # there is two way of formating one is using .format() and another is f infront of it
# c=f"mero name {m} ho {my_string} {a}"
# print(c)

# # replacement of string 
# my_string=my_string.replace("Hello","Namaste!")
# print(my_string)

# # counting of word inside the string
# print("number of o in string: ",my_string.count("o"))

# my_another="     ab,ababa,abab,baba"
# print("number of ab: ",my_another.count("ab"))

# # strip is used to print string properly in above space is not shown using strip
# print(my_another.strip())

# # split used to seprate the string in indexing form
#  print(my_string.split())

# # for indexing of string 
# for index,iterm in enumerate(my_string):
#     print("index of every string:",index,iterm)

# for making upper in split string  having even number of position
# mmy=my_string.split()
# for index,item in enumerate(mmy):
#     if index % 2 == 0:
#         mmy[index] = item.upper() 
# print(mmy)

# # 
# b=[item.upper() for item in mmy if mmy.index(item) % 2 ==0]
# print(b)

