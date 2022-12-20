
# price_of_iterm = {
#             'apple': 120,
#             'banana': 330,
#             'orange': 210,
#             'pear': 210,
#             'grape': 410,
#             'pineapple': 560,
#             'strawberry': 770,
#             'watermelon': 660
# }
# item_dict = {} #empty dictionary
# # for k, v in price_of_iterm.items():
# #     v = v + v*0.15
# #     print(v)
# #     # item_dict[k]= v

# #     # price_of_iterm.update({k:v})
# # print(item_dict)
# # # print(price_of_iterm)
# item_dict = {k : v+v*0.13 for k,v in price_of_iterm.items()} #same operation but in same line(dictionary comprehension)
# print(item_dict)
# # if you want to change the name also then use below code
# # iterm_dict = {f"{key}'s" : value+value*0.13 for key,value in price_of_iterm.items()}

# def get_price_of_iterm(iterm, tax_rate = 0.13):
#     return{k : v+v*tax_rate for k, v in iterm.items()}

# print(get_price_of_iterm(price_of_iterm,0.15))

# def fun(x):
#     f = x*x+5*x+1
#     print(f)
# x = int(input("enter the value: "))
# fun(x)

f = lambda x : x**2 + 5 *x  + 1
print(f(1))

# g = lambda name : name + name + "1"
# print(g("Pawan"))

h = lambda x, y : x**2 + 5*x*y +1
print(h(4,5))

