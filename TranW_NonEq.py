import numpy as np
import math 
import random
from numpy import linalg 
from numpy import real
from scipy import linalg, matrix
from sympy import Matrix
A={0:(0,1), 1:(2,3), 2:(0,2), 3:(0,3), 4:(1,2), 5:(1,3)}

def distance(X1,X2):
	Sum=0.0
	for i in range(len(X1)):
		Sum=Sum+(X1[i]-X2[i])*(X1[i]-X2[i])

	return math.sqrt(Sum/len(X1))



def OrderSets():
#	List=[0]*6
	Allset=[]
	List=[]
#	Allset.append(List)
#	print Allset
	NewSet=[]
	Set(Allset,List,0)
	for i in range(len(Allset)):
#		print list(reversed(Allset[i]))
		NewSet.append(Allset[i])
#		print Allset[i]
#		NewSet.append(list(reversed(Allset[i])))
#	print list(reversed(NewSet))
	return NewSet
#	return NewSet


def AllSets():
#	List=[0]*6
	Allset=[]
	List=[]
#	Allset.append(List)
#	print Allset
	NewSet=[]
	Set(Allset,List,0)
	for i in range(len(Allset)):
#		print list(reversed(Allset[i]))
#		print Allset[i]
		NewSet.append(list(reversed(Allset[i])))
#	print list(reversed(NewSet))
	return NewSet

def Set(Allset,List,index):
#	print index
	if len(List)==6:
		Allset.append(List)
	else:
		for i in range(2):
			Set(Allset,List+[i],index+1)
## Indexing the states ## 
def state(N1):
	N=list(reversed(N1))
	L=2**N[0]
	for i in range(1,len(N)):
		L=L+N[i]*(2**((i)*N[i]))
	return L-1

#def AllSol():
#	All=AllSets()
#	for i in All:
def getKey(item):
    return item[0]


def PrintALL():
	W=np.zeros((64, 64))
	New=AllSets()
	for i in New:
		Nb(i, W)
	return W 

def printW(W, size, index):
	s=''
	Iter=0
	if index==3 or index == 4:
		Iter=1
	iB=size*Iter+1
	Iter=0
	if index==2 or index == 4:
		Iter=1

	jB=size*Iter+1
	for i in range(iB,iB+size):
		for j in range(jB,jB+size):
			if W[i][j]==1.0:
#				print W[i][j]
				wxy="1"						
			elif W[i][j]==0.0:
				wxy="0"			
			elif W[i][j]==0.33:
				wxy="\\frac{1}{3}"
			elif W[i][j]==1.5:
				wxy="\\frac{3}{2}"
			elif W[i][j]==2.0:
				wxy="2"
			elif W[i][j]==0.83:
				wxy="\\frac{5}{6}"				
			elif W[i][j]==0.67:
				wxy="\\frac{2}{3}"
			elif W[i][j]==1.33:
				wxy="\\frac{4}{3}"
			elif W[i][j]==0.5:
				wxy="\\frac{1}{2}"
			else:
				wxy=str(W[i][j])
			if j!=jB+size-1:
				s=s+wxy+"&"								
			else:
				s=s+wxy+" \\"+"\\"+"\n"
#				print j
#				print W[i][j]
	print s

def printWALL(W, size):
	s=''
	for i in range(1,1+size):
		for j in range(1,1+size):
			if W[i][j]==1.0:
#				print W[i][j]
				wxy="1"						
			elif W[i][j]==0.0:
				wxy="0"			
			elif W[i][j]==0.33:
				wxy="\\frac{1}{3}"
			elif W[i][j]==1.5:
				wxy="\\frac{3}{2}"
			elif W[i][j]==2.0:
				wxy="2"
			elif W[i][j]==0.83:
				wxy="\\frac{5}{6}"				
			elif W[i][j]==0.67:
				wxy="\\frac{2}{3}"
			elif W[i][j]==1.33:
				wxy="\\frac{4}{3}"
			elif W[i][j]==0.5:
				wxy="\\frac{1}{2}"
			else:
				wxy=str(W[i][j])
			if j!=size:
				s=s+wxy+"&"								
			else:
				s=s+wxy+" \\"+"\\"+"\n"
	print s



def printZeroIndex(W, size):
	s=''
	for i in range(0,size):
		for j in range(0,size):
#			print W[i,j]
			if W[i,j]==1.0:
#				print W[i][j]
				wxy="1"						
			elif W[i,j]==0.0:
				wxy="0"			
			elif W[i,j]==0.33:
				wxy="\\frac{1}{3}"
			elif W[i,j]==1.5:
				wxy="\\frac{3}{2}"
			elif W[i,j]==2.0:
				wxy="2"
			elif W[i,j]==0.83:
				wxy="\\frac{5}{6}"				
			elif W[i,j]==0.67:
				wxy="\\frac{2}{3}"
			elif W[i,j]==1.33:
				wxy="\\frac{4}{3}"
			elif W[i,j]==0.5:
				wxy="\\frac{1}{2}"
			else:
				wxy=str(W[i,j])
			if j!=size-1:
				s=s+wxy+"&"								
			else:
				s=s+wxy+" \\"+"\\"+"\n"
	print s


'''
			if W[i][j]==0.0:
				wxy="0"			
			elif W[i][j]==0.33:
				wxy=" \\frac{1}{3} "
			elif W[i][j]==1.33:
				wxy=" \\frac{4}{3} "
			elif W[i][j]==0.5:
				wxy=" \\frac{1}{2} "
			else:
'''				

def Nb(N1, W):
	L1=state(N1)
	Neig=[]
	k=[0]*4
#	Neig.append(N1)
	for i in range(len(N1)):
		Neig.append(N1[:i]+[1-N1[i]]+N1[i+1:])

	k[0]=N1[0]+N1[2]+N1[3]
	k[1]=N1[0]+N1[4]+N1[5]
	k[2]=N1[2]+N1[4]+N1[1]	
	k[3]=N1[3]+N1[5]+N1[1]	

	Grand=[]
	Grand.append(stay(N1,k))
	for i in Neig:
		Z=Tran(N1,i,k)
		Grand.append(Z)
	Grand1=sorted(Grand,key=getKey)	
	s=''
	for i in range(len(Grand1)-1):
		(x,y)=Grand1[i]
		W[L1][x]=y
		s=s+'('+str(L1)+','+str(x)+') = '+str(y)+'&'
	(x,y)=Grand1[len(Grand1)-1]
	W[L1][x]=y	
	s=s+'('+str(L1)+','+str(x)+') = '+str(y)+" \\"	
	s=s+"\\"
#	print s

	s1="Transition from state " +str(L1)+", "+"$"+str(N1)+"$:"
#	print s1

	s2="\\begin{equation} \\nonumber \n"+"W("+str(L1)+",:)=c\n"+"\\begin{pmatrix}\n"
	s3=s+"\n"+"\end{pmatrix} \n"+"\end{equation} \n"

	S=s1+"\n"+s2+s3

#	print s
#	print s2
#	print s3
#\begin{pmatrix}

#\begin{equation}\nonumber 
#W(6,:)=c
#\begin{pmatrix}
#(6,2)= 0.5 & (6,5)= 1.5 & (6,6)= 0 & (6,8)= 0.83 & (6,14)= 0.33 & (6,22)= 0.5 & (6,38)= 0.33 \\
#\end{pmatrix}
#\end{equation}



#	print Grand
#	print Grand1


#	for i in range(4):
#		k[i]=+
#	return Neig

def stay(N1,k):
	L1=state(N1)
	prob=0
	if k[0]==0:
		prob=prob+1
	if k[1]==0:
		prob=prob+1
	if k[2]==3:
		prob=prob+1
	if k[3]==3:
		prob=prob+1
	prob=float(format(prob,'.2f'))
	if prob==0:
		prob=0
#	if prob==1.0:
#		prob=1

#	print(L1,prob)		
	return (L1,prob)

def Tran(N1,N2,k):
	prob=0
	L1=state(N1)
	L2=state(N2)

	index=[]
	for i in range(len(N1)):
		if N1[i]!=N2[i]:
#			index.append(i)
			if N1[i]==0:
#				print i
				if i in range(2,6):
					(x,y)=A[i]
					prob=1.0/(3-k[y])

				if i==0:
					prob=0

				if i==1:
					(x,y)=A[i]	
#					print A[i]				
					prob=1.0/(3-k[y])+1.0/(3-k[x])
#					print prob

			else:
				if i in range(2,6):
					(x,y)=A[i]
					prob=1.0/(k[x])

				if i==0:
					(x,y)=A[i]
#					print(x,y)
#					print(k[x],k[y])					
					prob=1.0/(k[y])+1.0/(k[x])

				if i==1:
					prob=0
	prob=float(format(prob,'.5f'))
	if prob==0:
		prob=0
#	if prob==1.0:
#		prob=1

#	print(L1,L2,prob)	
	return (L2,prob)

#	return index 
#	print L1
#	print L2

#print Tran([0,0,0,0,0,0],[0,1,0,0,0,0])
#print Tran([0,0,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0])
#stay([1,0,0,0,0,0],[0,0,0,0])
#AllSets()
W=PrintALL()
#print W
B=np.matrix(W)
A=B.T
#print A[16,16]
#printZeroIndex(A[16:32,16:32],16)
#for i in range(16,32):
#	for j in range(16,32):
#		print(i-15,j-15,A[i,j])
#	print "####"

C=A
#A = np.matrix([[0.25,0.25,0.5] , [0.1,0.8,0.1] , [0.6,0.3,0.1]])
#B = np.matrix([[0.25,0.25,0.5] , [0.1,0.8,0.1] , [0.6,0.3,0.1]])
#print B
X0 = np.random.random((64,1))
#X0=np.matrix(X0)
iterations = 20000
#print X0
for i in range (iterations):
	y = A*X0
#	print y
#	print max(y)
	X1=y/max(y)
	A = A*A		
	if distance(X1,X0) < 10**-8:
#		print i
		break
	X0=X1	

#print max(y)
#print X0
Sum=sum(X0)
X0= X0/Sum
#print X0

Sets=OrderSets()
Sum=0
for i in range(len(X0)):
	if X0[i] < 0.01:
		Z=0
#			print(i+1,Sets[i],0)
	else:
		prob=float(format(X0.item(i),'.5f'))
		Sum=Sum+prob
#		print(i+1,Sets[i],prob)

F=np.zeros((16,16))#,np.dtype('float64'))
#print F
for i in range(16,32):
	for j in range(16,32):
		F[i-16,j-16]=C[i,j]*X0[j]-C[j,i]*X0[i]
		if F[i-16,j-16] < 10**-6:
			F[i-16,j-16]=0
#print F
printZeroIndex(F,16)
#print Sum
#print max(y)
#X=C*X0
#print distance(X0,Xvi )
#print X
#print max(y)
#print X
#print B*X
#print max(y)

#print B
#print A


#for i in range(len())
#printW(W,32,4)
#printWALL(W,64)
#Nb([1,0,1,0,0,0])
