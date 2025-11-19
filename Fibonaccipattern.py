'''In a game, bonus points for each level follow a Fibonacci pattern.
Write a program to calculate the bonus for level N. Take level number as user input.'''

n=int(input("Enter the Bonas point: "))
if n<=0:
     print("Invalid")
elif n==1 or n==2:
 print("Bonas point=",1)
else:
    a,b=1,1
    for i in range(3,n+1):a,b=b,a+b
    print("Bonas point=",b)

