# class sagarmatha:
#     def __init__(self):
#         print("constructor created")
#     def home(self):
#         print("Home")
#     def __del__(self):
#         print("distructor")

# sg = sagarmatha()
# sg.home()

class details:
    def __init__(self, name, roll, faculty):
        self.name = name
        self.roll = roll
        self.faculty = faculty
    def view(self, name, roll):
        print(f"My name is {self.name} roll is {self.age}")
    def __del__(self):
        print("distructor")

name = input("\nEnter name : ")
roll = input("\nroll no :")
faculty = input("\n enter faculty: ")
de = details(name,roll, faculty)
details.view()

     


