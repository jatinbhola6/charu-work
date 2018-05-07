import pandas as pd
import numpy as np

def assign_cluster(data_row,mean_df):
    """
    takes one data row.
    find eucladian distance of the data row with center point of each cluster,
    and returns the cluster with closest center.
    """
    return mean_df.apply(lambda mean_row: round(np.sum((data_row-mean_row)**2)**0.5,2),axis=1).idxmin()
    
def get_mean(cluster_row,dataset):
    """
    takes a cluster and 
    calculates mean of all the datapoints in that cluster.
    """
    return dataset.loc[dataset['cluster']==cluster_row.name].mean().drop('cluster')

def main(dataset,no_cluster):
    """
    takes a dataset and number of clusters to be made,
    infinite loop will start until ceters stops changing on each iteration.
    works in three steps: 
        1. associate clusters to each datapoint.
        2. get cemter of each cluster
        3. check if centers changed. stop if means didn't change.
    """
    mean_df = dataset.sample(no_cluster)
    mean_df.index = range(no_cluster)
    calc_mean = None
    iter_count = 0
    while not mean_df.equals(calc_mean) :
        calc_mean = mean_df
        dataset['cluster'] = dataset.drop('cluster',errors='ignore').apply(assign_cluster,axis=1,mean_df=mean_df)
        mean_df = mean_df.apply(get_mean,axis=1,dataset=dataset)
        mean_df = mean_df.dropna(axis=0,how='any')
        iter_count += 1
    return dataset,iter_count