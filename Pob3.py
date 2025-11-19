""". A theatre stores booked seat numbers in an array.
Write a program to check if a particular seat number is already booked or not. Show the result."""


Store_set=[20,30,40,50,60,70,80]
Number=int(input("Enter a particular seat number:"))
if Number in Store_set:
    print(f"The seat:{Number} is already booked")
else:
    print(f"The seat: {Number} is not booked")