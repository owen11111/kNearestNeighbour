import matplotlib.pyplot as plt

#Determine the number of dimensions that we are working with
dims = 3

# Declare the dataset
dataset = [
    (1, 4, 14, 'A'),
    (2, 5, 10, 'A'),
    (7, 12, 15, 'B'),
    (10, 8, 5, 'A'),
    (15, 18, 20, 'B'),
    (1, 3, 8, 'A'),
    (4, 9, 12, 'B'),
    (12, 14, 18, 'A'),
    (19, 17, 3, 'B'),
    (6, 4, 14, 'A'),
    (11, 13, 7, 'B'),
    (8, 6, 2, 'A'),
    (3, 7, 17, 'B'),
    (17, 15, 11, 'A'),
    (14, 11, 6, 'B'),
    (0, 2, 13, 'A'),
    (5, 10, 16, 'B'),
    (13, 16, 1, 'A'),
    (18, 20, 4, 'B'),
    (9, 1, 9, 'A'),
    (16, 19, 19, 'B')
]

# Determine the target entry
datapoint1 = (5,7,15)

# Organise the dataset so it is usable for plotting
x, y, z, lab = ([data[i] for data in dataset] for i in range(dims+1))

# Create a list of lists of coordinates that can be used to 
coords = [[x[i], y[i], z[i]] for i in range(len(dataset))]

# Calculate the euclidean distance from the target variable to each of the datapoints in the 
# dataset then append these to a list of tuples containing distance, label and index
dists = []
for i in range(len(coords)):
    #######
    # Modify this code to change the distance metric used
    #######
    sumE = 0
    for j in range(dims):
        sumE = sumE + ((datapoint1[j] - coords[i][j]) ** 2)
    overallEucl = sumE ** 0.5

    dists.append((overallEucl, lab[i], i))

# Create a matplotlib graph to visualise this 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')

# Plot each point with respective color based on category
for i in range(len(dataset)):
    if lab[i] == 'A':
        ax.scatter(x[i], y[i], z[i], color='blue', label='A', s=50)
    else:
        ax.scatter(x[i], y[i], z[i], color='red', label='B', s=50)

# Plot the target datapoint using a separate colour
ax.scatter(datapoint1[0], datapoint1[1], datapoint1[2], color='green', s=50)

# Sort the distances so that we can get the k nearest
dists.sort(key=lambda x:x[0])

# Determine how many nearest neighbors we are looking for and add a small gold 
# circle to all that are under consideration, add their labels to a list of 
# nearest labels
k = 3
nearestLabels = []
for i in range(k):
    ind = dists[i][2]
    ax.scatter(x[ind], y[ind], z[ind], color='gold', s=5)
    nearestLabels.append(lab[ind])
    
# Sort the nearest labels so that we can find the centre of the 2 class problem, this 
# is the majority class
nearestLabels.sort(key= lambda x:x)

# Add a coloured circle to the target variable to represent the majority class
if(nearestLabels[int(k/2)]) == 'A':
    ax.scatter(datapoint1[0], datapoint1[1], datapoint1[2], color='blue', s=5)
else:
    ax.scatter(datapoint1[0], datapoint1[1], datapoint1[2], color='red', s=5)

plt.show()
