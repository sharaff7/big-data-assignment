from sklearn.cluster import KMeans
import numpy as np

def perform_kmeans(df):
    df_cleaned = df.dropna()

    numeric_columns = df_cleaned.select_dtypes(include=[np.number]).columns
    df_numeric = df_cleaned[numeric_columns]

    k = 3  
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df_numeric)

    cluster_labels = kmeans.labels_

    cluster_counts = np.bincount(cluster_labels)

    with open("k.txt", "w") as f:
        for cluster, count in enumerate(cluster_counts):
            f.write(f"Cluster {cluster}: {count} records\n")

    print("K-means clustering completed. Cluster counts saved as k.txt")
