import sys
import os

prime={}
list=[2,3,5,7,11,13,17,19]
for num in range(2,21):
	if num in list:
		prime[num]=1
	else:
		primenum={}
		ceiling=int(num**0.5)
		j=0
		while list[j]<=ceiling and list[j]<=num and num>=2:
			print list[j],num
			if num in list:
				if num not in primenum:
					primenum[num]=1
				else:
					primenum[num]+=1
				break
			while num%list[j]==0:
				if list[j] not in primenum:
					primenum[list[j]]=1
				else:
					primenum[list[j]]+=1
				num=num//list[j]
			j+=1
		for (val,count) in primenum.items():
			if val not in prime:
				prime[val]=primenum[val]
			if primenum[val]>prime[val]:
				prime[val]=primenum[val]
print prime
ans=1
for (val,count) in prime.items():
	ans=ans*(val**count)
print ans



