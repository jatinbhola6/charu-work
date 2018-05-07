#Aim:To implement Kmedioid clustering algorithm


import odict
import math
import random
#===============================================================================================================


def call_diff(a, clusters): #This method will determine the cluster in which an element will to go to
	
	dist=0.0
	val=0
	fr=0
	for i in clusters:
		x,y =a
		name,mean,temp_list=clusters[i]
		q,r=mean
		d=round(math.sqrt(pow(x-q,2)+pow(y-r,2)),2)
		if(fr==0):
			dist=d
			val=name
		if(d<dist):
			dist=d
			val=name
		fr=1
	return (val, dist)

#===========================================================================================
def call_mean(clusters, name_cord): # This method will determine intermediate mean values
	new_mean={}
	
	for i in clusters:
		x=0.0
		y=0.0
		name,mean,temp_list=clusters[i]
		l=len(temp_list)
		if (l!=0):
			for j in temp_list:
				q,r=name_cord[j]
				x=x+q
				y=y+r
			x=round(x/l,2)
			y=round(y/l,2)
			u,v=mean
			d=round(math.sqrt(pow(x-u,2)+pow(y-v,2)),2)
			new_mean[i]=(name,(x,y),mean,d)#name,new,old,diff
			#print str(mean)+"======"+str((x,y))
		
		
	return new_mean





	
#========================================================================================================
def check_termination(mean): #This checks if previous k ie. tempk and current k are same.Used as terminating case.
	for i in mean:
		name,new,old,dist=mean[i]
		if(new==old):
			continue
		else:
			return 0
	return 1
		
#===========================================================================================================

def compute_initial_cluster(name_cord, cluster):	
	n=len(name_cord)
	d=0
	name_dist_list=[]  #[distance, name]

	'''
	print "passed list of nodes"
	for i in name_cord:
		print i, name_cord[i]

	'''
	for i in name_cord:
		x,y=name_cord[i]
		d=int(pow(pow(x-0,2)+pow(y-0,2),0.5))
		name_dist_list.append((d,i))
	
	'''
	print "passed list nodes by distance"
	for i in range(0,n):
		print name_dist_list[i]
	'''


	name_dist_list.sort()	
	'''
	print "passed list nodes sorted by distance"
	for i in range(0,n):
		print name_dist_list[i]

	print	"=========================================="
	'''	
	a=0	
	c=n//cluster
	
	center_list=[]	#list of centers (distance, name)
	cluster_list=[]
	temp_cluster_list=[]
	temp_list=[]
	for i in range(0,cluster):
		center_dist, center_name=name_dist_list[a+c/2]
		center_list.append(name_cord[center_name])
		a=a+c


	#center_list=[]	
	#center_list=[(3, 1),(10,12),(3,4),(15,4)]
	
	cluster_name_list=[]	
	for i in range(0,cluster):
		cluster_name_list.append('c'+str(i))
	
		

	clusters={}
	for i in range(0,cluster):
		clusters[cluster_name_list[i]]=(cluster_name_list[i],center_list[i],[])

	return clusters
			
#==========================================================================================================
def main(name_cord, cluster):
	
	
		
	#name_cord dictionary name as key
	

        #initial assignment
	clusters=compute_initial_cluster(name_cord, cluster)
	alt={}	
	for i in name_cord:
		alt[i]=name_cord[i]
	
	
	aa=0
	flag=0
	gt=0
	f=0
	while(flag==0):	
		for i in name_cord: # for loop will cal cal_diff(int) for every element.
			
			if(f!=0):
				p_cluster_name, p_dist_from_cluster=alt[i]					
			cluster_name, dist_from_cluster1=call_diff(name_cord[i], clusters)#temp will tell in which cluster element will go to
			
			cluster_name,mean,temp_list=clusters[cluster_name]
			gt=gt+cluster
				
			if(f!=0):
				if(p_cluster_name==cluster_name):
					#print str(i)+"--------in--------"+str(mean)
					continue
				else:
					p_cluster_name,p_mean,p_temp_list=clusters[p_cluster_name]
					p_temp_list.remove(i)
					clusters[p_cluster_name]=(p_cluster_name,p_mean,p_temp_list)
			
			#print str(i)+"--------in--------"+str(cluster_name)
			temp_list.append((i))	
			clusters[cluster_name]=(cluster_name,mean,temp_list)
			alt[i]=(cluster_name,dist_from_cluster1)
			
		'''
		for i in clusters:
			name,mean,temp_list=clusters[i]	
			print str(name)
			print "=======================>"
			print temp_list
		print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		'''
				


		f=f+1	
		
		new_mean=call_mean(clusters, name_cord)
		flag=check_termination(new_mean)
		if(flag==1):
			u=len(name_cord)
			print u
			u=u*cluster
			u=u*f
			
			#red=random.randint(500,u)
			#gt=gt-red
			#print str(f) +" MMMMMMMMMMMMMMM"+str(gt)
			return (gt,f,clusters)
		else:
					
			for i in new_mean:
				name,new,old,dist=new_mean[i]
				cluster_name,mean,temp_list=clusters[i]
				clusters[i]=(cluster_name,new,temp_list)
				'''print "MMMMMMMMMMMMMMM"
				print "no--------->"+str(f)
				print "cluster name--------->"+str(name)
				print "old========>"+str(old)
				print "new========>"+str(new)
				'''
	

	




















