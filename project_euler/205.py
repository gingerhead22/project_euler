import sys
import os

Peter=[0 for i in range(37)]

Colin=[0 for j in range(37)]

pyra=[1,2,3,4]

for dice1 in pyra:
	for dice2 in pyra:
		for dice3 in pyra:
			for dice4 in pyra:
				for dice5 in pyra:
					for dice6 in pyra:
						for dice7 in pyra:
							for dice8 in pyra:
								for dice9 in pyra:
									sum=dice1+dice2+dice3+dice4+dice5+dice6+dice7+dice8+dice9
									Peter[sum]=Peter[sum]+1


cube=[1,2,3,4,5,6]

for dice1 in cube:
	for dice2 in cube:
		for dice3 in cube:
			for dice4 in cube:
				for dice5 in cube:
					for dice6 in cube:
						sum=dice1+dice2+dice3+dice4+dice5+dice6
						Colin[sum]+=1

#print type(Peter)
totalP=4**9

for i in range(len(Peter)):
	Peter[i]=float(Peter[i])/float(totalP)


totalC=6**6
for i in range(len(Colin)):
	Colin[i]=float(Colin[i])/float(totalC)


#print Peter
#print Colin

P=0
for i in range(len(Peter)):
	for j in range(i):
		P+=Peter[i]*Colin[j]
print P