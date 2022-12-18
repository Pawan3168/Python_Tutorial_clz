# # # addition of items in dictionary
# # classmate = {"Manoj":1, "Pawan":2}
# # print(classmate)
# # classmate["sumit"] = 3  #added the item in dictionary 
# # print(classmate)
# # classmate["Pawan"] = 4 #changes the value of key pawan
# # print(classmate)
# # print(classmate.items()) #it shows the items inside the dictionary
# # print(classmate["Manoj"] == 1) #it shows the value of key is true or false
# # print(classmate["Manoj"] == 12) #false
# # classmate.pop("sumit") #it delete the key and value from dictionary
# # print(classmate)
# # print(len(classmate)) #length of dictionary
# # classmate["name"] = "Ram"
# # print(classmate)
# # classmate.popitem() #it pop out the last value and key 
# # print("pop the last ram: ",classmate)
# # print(classmate.get("Manoj")) #getting the value of key manoj
# # classmate["Benchmate"] = {"sanket", "sagarmatha", "anything"} #nested dictionary dictionary inside dictionary
# # print(classmate)
# sagarmatha = {
#         "Education Department": {
#                 "Computer Science": {
#                         "HOD":"Bharat Bhatta", 
#                         "no_of_students": 100
#                 },
#                 "Civil": {
#                         "HOD":"Sudip Lamsal",
#                         "no_of_students": 200
#                 }
#         },
#         "Admin Department": {
#                 "Accounts": {
#                         "HOD":"Chaturbhuj Nepali",
#                         "no_of_students": 50
#                 }
#         }
# }
# print(sagarmatha["Education Department"]["Computer Science"]["HOD"]) #printed the nested dictionary
# print(sagarmatha["Education Department"]["Civil"]["HOD"])
