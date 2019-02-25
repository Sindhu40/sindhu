a=int(input("Please enteri first number of an A.P Series: : "))
n=int(input("Please enter the total numbers in this A.P Series: : "))
d=int(input("Please enter the Common Difference : "))
total=(n * (2 * a + (n - 1) * d)) / 2
tn=a + (n - 1) * d
print("The Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)
