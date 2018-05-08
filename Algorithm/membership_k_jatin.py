import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def compute_initial_cluster(dataset,no_cluster):
	dataset["cartesian"] = dataset.apply(lambda x: int(np.sum(x**2)**0.5),axis=1)
	a = 0
	c = dataset.shape[0]//no_cluster
	clusters = pd.DataFrame()
	for _ in range(no_cluster):
		clusters = clusters.append(dataset.sort_values('cartesian').drop(["cartesian"],errors="ignore",axis=1).loc[int(a+c/2)])
		a = a+c
	clusters.index = range(no_cluster)
	return clusters
def initialize_member(dataset,clusters,no_cluster):
	return pd.DataFrame(euclidean_distances(dataset,clusters),index=dataset.index.values,columns=clusters.index.values),pd.DataFrame(np.zeros((dataset.shape[0],no_cluster)),index = dataset.index.values,columns=range(no_cluster))

def main(dataset,no_cluster,threshold):
	iter_count = 0
	clusters = compute_initial_cluster(dataset,no_cluster)
	dataset = dataset.drop(['cartesian'],axis=1)
	cluster_dist,cluster_counter = initialize_member(dataset,clusters,no_cluster)
	flag = False
	while flag != True:  
	    for didx,drow in dataset.drop(['clusters'],errors='ignore').iterrows():
	        for cidx,cluster in clusters.iterrows():
	            if cluster_counter.loc[didx,cidx] <= threshold:
	                dist = np.sum((drow-cluster)**2)**0.5
	                if dist > cluster_dist.loc[didx,cidx]:
	                    cluster_counter.loc[didx,cidx] += 1
	                    if cluster_counter.loc[didx,cidx]<=threshold:
	                        cluster_dist.loc[didx,cidx] = dist
	                    else:
	                        cluster_dist.loc[didx,cidx] = np.inf
	                else:
	                    cluster_dist.loc[didx,cidx] = dist
	            else:
	                cluster_dist.loc[didx,cidx] = np.inf
	    dataset['clusters'] = dataset.apply(lambda row:cluster_dist.loc[row.name,cluster_counter.loc[row.name] <= threshold].idxmin(),axis=1)
	    new_clusters = clusters.apply(lambda cluster_row: dataset.loc[dataset['clusters']==cluster_row.name].mean().drop('clusters'),axis=1)
	    if new_clusters.equals(clusters):
	        flag = True
	    else:
	        clusters = new_clusters
	    iter_count += 1
	return dataset,iter_count