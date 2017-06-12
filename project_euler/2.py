import sys
import os

ceiling=4000000

sum=0

a,b=1,2

while b<=ceiling:
	if b%2==0:
		sum+=b
	temp=b
	b=a+b
	a=temp
print sum
