import sys 
import os

file=open('13-input.txt','r')

ans=[0 for i in range(60)]
for c in range(100):
	line=file.readline()
	line=line[:-1]
	add=[]
	while len(line)>0:
		add.append(int(line[-1]))
		line=line[:-1]

	for j in range(len(add)):
		ans[j]=ans[j]+add[j]
		if ans[j]>=10:
			ans[j]-=10
			ans[j+1]+=1
if ans[j+1]>10:
	ans[j+1]=ans[j+1]%10
	ans[j+2]=ans[j+2]+ans[j+1]//10
	
while ans[-1]==0:
	ans.pop()
ans=ans[::-1]

res=''
for i in range(10):
	res=res+str(ans[i])
res=int(res)
print res