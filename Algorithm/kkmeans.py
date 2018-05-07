#Aim:To implement Kmeans clustering algorithm
from util import odict
import pandas as pd
import numpy as np

#===================================================================================================

def call_diff(a, m, n, p): #This method will determine the cluster in which an element will to go to
	
	#diff=[0.0]*p
	diff = [round(pow(sum([pow(a[j]-m[i][j],2) for j in range(p)]),0.5),2) for i in range(p)]
		
	val=0
	
	temp=diff[0]
	for i in range(0,p):	
		if(diff[i]<temp):
			temp=diff[i]
			val=i
	
	return val

#===========================================================================================
def call_mean(k, m, n, p): # This method will determine intermediate mean values

		
	m1 =[[0.0 for _ in i] for i in m]
	for i in range(0,p):
		c=0
		x=0.0
		y=0.0
		for j in range(0,n):
			for l in range(len(m[i])):

			if(k[i][j] == -1):
				break
			else:
				q,r=k[i][j]
				x=x+q
				y=y+r
				m1[i]=(x,y)
				c=c+1
		if(c!=0):
			x,y=m1[i]
			x=round(x/c,2)
			y=round(y/c,2)		
			m1[i]=(x,y)
	#for i in range(0,p):
		#print str(m[i])+"-----------"+str(m1[i])	
	
	return m1
		
	
#==============================================================================================
def check_termination(k, tempk): #This checks if previous k ie. tempk and current k are same.Used as terminating case.
	
	if(tempk==k):
		return 1
	return 0
	
#==========================================================================================================
def main(cwd, p):
		
	
	n = cwd.count
	#k=[[-1 for _ in xrange(n)] for _ in xrange(p)]
	k = np.one((p,n))*-1
	tempk=np.one((p,n))*-1
		
	
	temp=0
	flag=0
	#m=[(0.0,0.0)]*p	#mean
	m = [tuple([0.0]*len(cwd['n1']))]*p
	
	t_t=0	
	for i in cwd:	#initializing means with first p nodes. 
		if(t_t<p):
			m[t_t]=cwd[i]
			t_t=t_t+1	

	gt=0
	r=0
	while (flag==0): #infinite loop, until algo stabilizes
		
		tt=[0]*p #to keap track how many elements in any cluster
		
		
		r=r+1
		
		
		cluster_list=[0]*p #declaring cluster list
		for i in range(0,p):
			cluster_list[i]=odict.OrderedDict() #initializing cluster list with dictionary

	
		k=[[-1 for _ in xrange(n)] for _ in xrange(p)]

		for i in cwd: # for loop will cal cal_diff(int) for every element.
		
						
			temp=call_diff(cwd[i], m, n, p)#temp will tell in which cluster element will go to
			gt=gt+p
			
			k[temp][tt[temp]]=cwd[i]
			tt[temp]=tt[temp]+1
			cluster_list[temp][i]=i
		
		

		m=call_mean(k, m, n, p) # call to method which will calculate mean at this step.
		flag=check_termination(k,tempk) # check if terminating condition is satisfied.
		if(flag != 1):
			#Take backup of k in tempk so that you can check for equivalence in next step*/
			tempk=k


		
	#print "no of loops==========>"+str(r)
	#print "final means===>"
	#print m
	
	return (gt, r, cluster_list)
		
#========================================================
#call main() 

if __name__ == "__main__":
	main()


