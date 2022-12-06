# python is dynamic type 
# def is used as defining function
# write a program to check a number is palindrome or not using function
def palindrome(num):
    temp= num
    rev=0
    while num>0:
        dig =num%10
        rev=rev*10+dig
        print(num)
        num=num//10
        print(num)
    if temp==rev:
        return True
    else:
        return False
num=int(input("Enter the number: "))
if palindrome(num):
    print("the number is palindrome")
else:
    print("The number is not palindrome")