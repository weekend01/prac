import numpy as np

# Given points
points = {
    'P1': np.array([0.1, 0.6]),
    'P2': np.array([0.15, 0.71]),
    'P3': np.array([0.08, 0.9]),
    'P4': np.array([0.16, 0.85]),
    'P5': np.array([0.2, 0.3]),
    'P6': np.array([0.25, 0.5]),
    'P7': np.array([0.24, 0.1]),
    'P8': np.array([0.3, 0.2])
}

# Initial centroids
m1 = np.array([0.1, 0.6])  # Cluster 1 centroid
m2 = np.array([0.3, 0.2])  # Cluster 2 centroid

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Perform K-means clustering
iterations = 0
previous_m1, previous_m2 = m1.copy(), m2.copy()
clusters = {1: [], 2: []}

# Step 1: Assign points to the nearest centroid
while True:
    clusters = {1: [], 2: []}
    for point_name, point in points.items():
        dist_to_m1 = euclidean_distance(point, m1)
        dist_to_m2 = euclidean_distance(point, m2)
        
        # Assign point to nearest centroid
        if dist_to_m1 < dist_to_m2:
            clusters[1].append(point_name)
        else:
            clusters[2].append(point_name)
    
    # Step 2: Update centroids
    m1 = np.mean([points[p] for p in clusters[1]], axis=0) if clusters[1] else m1
    m2 = np.mean([points[p] for p in clusters[2]], axis=0) if clusters[2] else m2
    
    # Check if centroids have changed
    iterations += 1
    if np.allclose(m1, previous_m1) and np.allclose(m2, previous_m2):
        break
    
    previous_m1, previous_m2 = m1.copy(), m2.copy()

# Output results
print(f"Cluster 1 points: {', '.join(clusters[1])}")
print(f"Cluster 2 points: {', '.join(clusters[2])}")
print(f"Updated centroid m1: {m1}")
print(f"Updated centroid m2: {m2}")
print(f"Number of iterations: {iterations}")

# Part 1: Which cluster does P6 belong to?
P6 = np.array([0.25, 0.5])
dist_to_m1 = euclidean_distance(P6, m1)
dist_to_m2 = euclidean_distance(P6, m2)
cluster_P6 = 1 if dist_to_m1 < dist_to_m2 else 2
print(f"P6 belongs to Cluster {cluster_P6}")

# Part 2: Population of cluster around m2
population_cluster_around_m2 = len(clusters[2])
print(f"Population of cluster around m2: {population_cluster_around_m2}")
