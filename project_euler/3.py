import sys
import os

NUM=600851475143
ceiling=int(NUM**0.5)

factor=[]

for i in range(2,ceiling+1):
	if NUM%i==0:
		factor.append(i)
		NUM=NUM//i
print max(factor[-1],NUM)
