import sys
import os

def PI(start,end):
	ans=1
	for i in range(start, end+1):
		ans=ans*i
	return ans
print PI(21,40)/PI(1,20)