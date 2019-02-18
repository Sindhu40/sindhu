number = 407
number = int(input("enter a number: "))
if number > 1:
   for i in range(2,number):
       if (number % i)==0:
           print("number is not prime number")
           print(i,"times",number//i,"is",number)
           break
   else:
       print("number is prime number")
   else:
       print("number is not  prime number")
