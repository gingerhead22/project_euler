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

sum=5
num=4

while num<2000000:
	if isPrime(num):
		primelist.append(num)
		#print num
		sum+=num
	num+=1

print sum