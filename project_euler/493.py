import sys
import os

def production(start,end):
	ans=1
	for i in range(start,end+1):
		ans=ans*i
	return ans

def combinantion(k,n):
	return product(k+1,n)/product(1,k)

combination(2,7)*2*