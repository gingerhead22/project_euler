import sys
import os

def addtill(num):
	sum=0
	for i in range(1,num+1):
		sum+=i
	return sum

def main():
	count3=999//3
	count5=999//5
	count15=999//15
	ans=3*addtill(count3)+5*addtill(count5)-15*addtill(count15)
	print ans

if __name__=='__main__':
	main()