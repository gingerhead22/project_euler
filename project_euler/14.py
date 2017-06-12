import sys
import os

ceil=1000

tree=[[] for i in range(30*ceil+2)]
tree[0]=[0]
tree[1]=[1]
tree[2]=[2]
check=[0 for i in range(30*ceil+2)]
check[0]=check[1]=check[2]=1
count=2
level=2
p=[2]

def full(list):
	for item in list:
		if item==0:
			return False
	return True

while count<ceil or (not full(check[:ceil+1])):
	#isFull, remind=full(check[:1000001])
	x=p.pop(0)
	#print count,level,tree[level]
	level+=1
	y=2*x
	if y<=30*ceil+2 and check[y]==0 :
		count+=1
		check[y]=1
		tree[level].append(y)
		p.append(y)
	if (x-1)%3==0:
		z=(x-1)//3
	 	if z%2!=0 and z<=30*ceil+2 and check[z]==0:
			count+=1
			check[z]=1
			tree[level].append(z)
			p.append(z)

while tree[-1]:
	tree.pop()
find=False
while not find:
	for item in tree[-1]:
		if item<=ceil:
			find=True
			ans=item
			break
	tree.pop()
print ans, len(tree)

