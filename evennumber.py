start=int(input("enter the start of range:")) 
end=int(input("enter the end of range:"))  
for number in range(start,end+1): 
    if number % 2 == 0: 
        print(number,end=" ") 
