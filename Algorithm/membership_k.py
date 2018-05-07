#Aim:To implement Kmedioid clustering algorithm


import odict
import math
import simple_k_mean as skm
th=2


#===============================================================================================================


def call_diff(a, clusters): #This method will determine the cluster in which an element will to go to
	
	dist=0.0
	val=0
	fr=0
	clus={}
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
		clus[i]=(i,d,1)#clustern name, dist, count		
		fr=1
	return (val, dist, clus)
#=====================================================================
def call_diff_memb(a, clusters, clus): #This method will determine the cluster in which an element will to go to
	
	
	dist=0.0
	val=0
	fr=0
	remove=[]
	
	for i in clus:
		x,y =a
		cluster_name,old_dist,c=clus[i]
		cluster_name,mean,temp_list=clusters[cluster_name]
		q,r=mean
		d=round(math.sqrt(pow(x-q,2)+pow(y-r,2)),2)
		
		if(fr==0):
			dist=d
			val=cluster_name
		if(d<=dist):
			dist=d
			val=cluster_name
		fr=1
		
		
		if(d>=old_dist):
			
			if(c==20):
				#print "adddddddddd"
				remove.append(i)
			else:
				c=c+1
				clus[i]=(cluster_name,d,c)
		else:
			c=0
			clus[i]=(cluster_name,d,c)
			
			
	#print "for "+str(a)+"===>"+str(remove)	
	if len(remove)!=0:	
		for i in remove:
			clus.__delitem__(i)

	
	return (val, dist, clus)
	



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


			
#==========================================================================================================
def main(name_cord, cluster):
	
	
	clusters=skm.compute_initial_cluster(name_cord, cluster)
	alt={}	
	
	for i in name_cord:
		alt[i]=name_cord[i]
	
	
	for i in name_cord: # for loop will cal cal_diff(int) for every element.
						
		cluster_name, dist_from_cluster1, clus=call_diff(name_cord[i], clusters)#temp will tell in which cluster element will go to
		cluster_name,mean,temp_list=clusters[cluster_name]
	
		temp_list.append((i))	
		clusters[cluster_name]=(cluster_name,mean,temp_list)
		alt[i]=(cluster_name,dist_from_cluster1,clus)
		
		
	new_mean=call_mean(clusters, name_cord)
	for i in new_mean:
			name,new,old,diff=new_mean[i]
			cluster_name,mean,temp_list=clusters[i]
			clusters[i]=(cluster_name,new,temp_list)#updating mean

	flag=0
	f=0
	gt=0
	rm=[]
	while(flag==0):
				
		f=f+1
		

		#for i in rm:
		#	alt.__delitem__(i)

		
		rm=[]
		
		mf=0
		for i in alt:
			x,y=name_cord[i]
			p_cluster_name,p_dist_from_cluster,clus=alt[i]
			if(len(clus)==0):
				#print "same for "+str(i)+" in "+str(p_cluster_name)
				rm.append(i)
				continue
			p_cluster_name,p_mean,p_temp_list=clusters[p_cluster_name]
			p_cluster_name,new,old,diff=new_mean[p_cluster_name]
					
			
			cluster_name, dist_from_cluster1, clus=call_diff_memb(name_cord[i], clusters, clus)
			gt=gt+len(clus)
			
			
			alt[i]=cluster_name, dist_from_cluster1,clus
			
			cluster_name,mean,temp_list=clusters[cluster_name]
			if(p_cluster_name==cluster_name):
				#print "calculated same, same for "+str(i)+" in "+str(p_cluster_name)
				continue
			
			else:
								
				
				mf=1		
				p_temp_list.remove(i)
				clusters[p_cluster_name]=(p_cluster_name,p_mean,p_temp_list)
				temp_list.append((i))	
				clusters[cluster_name]=(cluster_name,mean,temp_list)
				
				
				
		
		
		new_mean=skm.call_mean(clusters, name_cord)
		flag=skm.check_termination(new_mean)
		if(mf==0):
			
			return (gt, f, clusters)
		else:
				
			for i in new_mean:
				name,new,old,diff=new_mean[i]
				cluster_name,mean,temp_list=clusters[i]
				clusters[i]=(cluster_name,new,temp_list)
				
				

def clf(clus):
	dd=[]
	
	for j in clus:	
		cluster_name,d,c=clus[j]
		dd.append(cluster_name)
	print str(dd)
	

def cf(alt,f):
	print "in loop===>"+str(f)
	for i in alt:
		dd=[]
		cluster_name, dist_from_cluster1,clus=alt[i]
		if (len(clus)<8):
			for j in clus:	
				cluster_name,d,c=clus[j]
				dd.append(cluster_name)
			print "member clusters "+str(i)+" data "+str(dd)
			print "...................................................."

