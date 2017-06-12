import sys
import os
N=15
file=open('18-input.txt','r')
triangle=[]
for n in range(N):
	line=file.readline().split()
	lines=[]
	for i in range(n+1):
		lines.append(int(line[i]))
	triangle.append(lines)

triangle=triangle[::-1]

print triangle

for level in range(1,15):
	for order in range(15-level):
		triangle[level][order]+=max(triangle[level-1][order],triangle[level-1][order+1])
print triangle[level][order]
