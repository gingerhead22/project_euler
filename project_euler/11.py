import sys
import os
def findHoriMax():
	ans=-1
	for i in range(20):
		max=-1
		product=-1
		line=matrix[i]
		j=0
		while j<=16:
			if max==-1 or line[j+3]>line[j-1]:
				product=line[j]*line[j+1]*line[j+2]*line[j+3]
			if max<product:
				max=product
		if ans<max:
			ans=max
	return ans
	
def findVertMax():

file=open('./11-input.txt','r')
matrix=[[]]
for i in range(20):
	line=file.readline().split()
	for j in range(20):
		matrix[i][j]=int(line[j])
