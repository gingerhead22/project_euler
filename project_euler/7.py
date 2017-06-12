import sys
import os

primelist=[2,3]

def isPrime(num):
	ceiling= int(num**0.5)
	check=True
	for prime in primelist:
		if prime <=ceiling and num%prime==0:
			check=False
			break
	return check

count=2
num=4

while count<10001:
	if isPrime(num):
		primelist.append(num)
		count+=1
	num+=1

print primelist[-1]