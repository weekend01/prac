import numpy as np

# Given points
points = {
    'P1': np.array([2, 10]),
    'P2': np.array([2, 5]),
    'P3': np.array([8, 4]),
    'P4': np.array([5, 8]),
    'P5': np.array([7, 5]),
    'P6': np.array([6, 4]),
    'P7': np.array([1, 2]),
    'P8': np.array([4, 9])
}

# Initial centroids
m1 = np.array([2, 10])  # Cluster 1 centroid
m2 = np.array([5, 8])   # Cluster 2 centroid
m3 = np.array([1, 2])   # Cluster 3 centroid

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Perform K-means clustering
iterations = 0
previous_m1, previous_m2, previous_m3 = m1.copy(), m2.copy(), m3.copy()
clusters = {1: [], 2: [], 3: []}

# Step 1: Assign points to the nearest centroid
while True:
    clusters = {1: [], 2: [], 3: []}
    for point_name, point in points.items():
        dist_to_m1 = euclidean_distance(point, m1)
        dist_to_m2 = euclidean_distance(point, m2)
        dist_to_m3 = euclidean_distance(point, m3)
        
        # Assign point to nearest centroid
        if dist_to_m1 < dist_to_m2 and dist_to_m1 < dist_to_m3:
            clusters[1].append(point)
        elif dist_to_m2 < dist_to_m1 and dist_to_m2 < dist_to_m3:
            clusters[2].append(point)
        else:
            clusters[3].append(point)
    
    # Step 2: Update centroids
    m1 = np.mean(clusters[1], axis=0) if clusters[1] else m1
    m2 = np.mean(clusters[2], axis=0) if clusters[2] else m2
    m3 = np.mean(clusters[3], axis=0) if clusters[3] else m3
    
    # Check if centroids have changed
    iterations += 1
    if np.allclose(m1, previous_m1) and np.allclose(m2, previous_m2) and np.allclose(m3, previous_m3):
        break
    
    previous_m1, previous_m2, previous_m3 = m1.copy(), m2.copy(), m3.copy()

# Output results
print(f"Cluster 1 points: {['P' + str(i+1) for i in range(len(clusters[1]))]}")
print(f"Cluster 2 points: {['P' + str(i+1) for i in range(len(clusters[2]))]}")
print(f"Cluster 3 points: {['P' + str(i+1) for i in range(len(clusters[3]))]}")
print(f"Updated centroid m1: {m1}")
print(f"Updated centroid m2: {m2}")
print(f"Updated centroid m3: {m3}")
print(f"Number of iterations: {iterations}")

# Part 1: Which cluster does P6 belong to?
P6 = np.array([6, 4])
dist_to_m1 = euclidean_distance(P6, m1)
dist_to_m2 = euclidean_distance(P6, m2)
dist_to_m3 = euclidean_distance(P6, m3)
cluster_P6 = 1 if dist_to_m1 < dist_to_m2 and dist_to_m1 < dist_to_m3 else (2 if dist_to_m2 < dist_to_m3 else 3)
print(f"P6 belongs to Cluster {cluster_P6}")

# Part 2: Population of cluster around m3
population_cluster_around_m3 = len(clusters[3])
print(f"Population of cluster around m3: {population_cluster_around_m3}")

