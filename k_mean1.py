import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
data = pd.read_csv('Countryclusters.csv')
x = data.iloc[:, 1:3]  # 1t for rows and second for columns
kmeans = KMeans(3)
means.fit(x)
identified_clusters = kmeans.fit_predict(x)
identified_clusters
array([1, 1, 0, 0, 0, 2])

data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters
plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],c=data_with_clusters['Clusters'],cmap='rainbow')