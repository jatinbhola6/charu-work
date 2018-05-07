import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def compute_initial_cluster(dataset,no_cluster):
    dataset["cartesian"] = dataset.apply(lambda x: int(np.sum(x**2)**0.5),axis=1)
    clusters = dataset.sort_values(by='cartesian').iloc[0::dataset.shape[0]/no_cluster].drop('cartesian',axis=1)
    dataset = dataset.drop('cartesian',axis=1)
    return clusters
def initialize_member(dataset,clusters,no_cluster):
    return pd.DataFrame(euclidean_distances(dataset,clusters),index=dataset.index.values,columns=clusters.index.values),
    pd.DataFrame(np.zeros((dataset.shape[0],no_cluster)),index = dataset.index.values,columns=range(no_cluster))