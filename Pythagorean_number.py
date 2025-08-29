'''triple of numbers (a,b,c) is called a Pythagorean triple if a*a+b*b=c*c.
In this question, you will be given three numbers.
You have to output 1 if the three numbers form a Pythagorean triple.
Otherwise, you have to output 0. Note that the inputs may not be given in order:
you may have to try all possible orderings of the three numbers to determine whether they form a Pythagorean triple.
 Input Three integers.
  Output 1 if the three numbers are part of a Pythagorean triple 0 otherwise'''

a=int(input())
b=int(input())
c=int(input())
d=a*a+b*b
e=c*c
print('output')
if d==e:
    print(1)
else:
    print(0)
