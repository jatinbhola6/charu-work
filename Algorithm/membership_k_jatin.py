import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def compute_initial_cluster(dataset,no_cluster):
	dataset["cartesian"] = dataset.apply(lambda x: int(np.sum(x**2)**0.5),axis=1)
	clusters = dataset.sort_values(by='cartesian').iloc[0::dataset.shape[0]//no_cluster][:no_cluster].drop(['cartesian'],axis=1)
	dataset = dataset.drop(['cartesian'],axis=1)
	clusters.index = range(no_cluster)
	return clusters
def initialize_member(dataset,clusters,no_cluster):
	return pd.DataFrame(euclidean_distances(dataset,clusters),index=dataset.index.values,columns=clusters.index.values),
	pd.DataFrame(np.zeros((dataset.shape[0],no_cluster)),index = dataset.index.values,columns=range(no_cluster))
def assign_cluster(data_row,mean_df):
	"""
	takes one data row.
	find eucladian distance of the data row with center point of each cluster,
	and returns the cluster with closest center.
	"""
	return mean_df.apply(lambda mean_row: round(np.sum((data_row-mean_row)**2)**0.5,2),axis=1).idxmin()
def main(dataset,no_cluster,threshold):
	clusters = compute_initial_cluster(dataset,no_cluster)
	cluster_dist,cluster_counter = initialize_member(dataset,clusters,no_cluster)
	while(flag != True):
		for didx,drow in dataset.drop(['clusters'],errors='ignore').iterrows():
			for cidx,cluster in clusters.iterrows():
				if cluster_counter.loc[didx,cidx] < threshold:
					dist = np.sum((drow - cluster)**2)**0.5
					if dist > cluster_dist.loc[didx,cidx]:
						if cluster_counter.loc[didx,cidx] < threshold:
							cluster_counter.loc[didx,cidx] += 1
						else: 
							cluster_dist.loc[didx,cidx] = np.inf
					else:
						cluster_dist.loc[didx,cidx] = dist
		dataset['clusters'] = dataset.apply(lambda row:cluster_dist.loc[row.name,cluster_counter.loc[row.name] < threshold].idxmin(),axis=1)
		new_clusters = clusters.apply(lambda cluster_row: dataset.loc[dataset['cluster']==cluster_row.name].mean().drop('cluster'),axis=1)
		if new_clusters.equals(clusters):
			flag = True
		else:
			clusters = new_clusters
	return dataset