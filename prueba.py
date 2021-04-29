#función para calcular la distancia entre los puntos
def distancia(a, b):
    sum = 0
    for i in range(len(b)):
        sum += (b[i] - a[i])**2
    return sum
  #Algoritmo de Kmeans
def kMeans(data, centroids):
    centroidsAsKeys = []
    for c in centroids:
        centroidsAsKeys.append(str(c))
    centroidsDict = {k:[] for k in centroidsAsKeys}
    
    # Datos más cercanos al centroide:
    for d in data:
        closestCentroid = centroids[0]
        smallestD = distancia(d, closestCentroid)
        for c in centroids:
            dist = distancia(d, c)
            if dist < smallestD:
                smallestD = dist
                closestCentroid = c
        centroidsDict[str(closestCentroid)].append(d)   
    return centroidsDict
  
  #Actualización de Centroides
def actualizaCentroides(theDict):
    newCentroids = []
    for key, pointsList in theDict.items():
        oldCentroid = key
        components = len(pointsList[0])
        newCentroid = []
        for c in range(components):
            newCentroid.append(pointsList[0][c])   
        for p in pointsList:
            for c in range(components):
                newCentroid[c] = newCentroid[c] + p[c] / 2.0
        newCentroids.append(newCentroid)
    return newCentroids
  
  def inicializacionCentroides(data, k):
    
    usedIndices = []
    centroidsAsKeys = []
    centroids = []
    for c in range(k):
        index = random.randrange(len(data))
        while index in usedIndices:
            index = random.randrange(len(data))
        usedIndices.append(index)
        centroid = data[index]
        centroids.append(centroid)
        centroidsAsKeys.append(str(centroid))
    centroidsDict = {k:[] for k in centroidsAsKeys}
    
    # Datos más cercanos al centroide:
    for d in data:
        closestCentroid = centroids[0]
        smallestD = distancia(d, closestCentroid)
        for c in centroids:
            dist = distancia(d, c)
            if dist < smallestD:
                smallestD = dist
                closestCentroid = c
        centroidsDict[str(closestCentroid)].append(d)   
    return centroidsDict
  
  
  
#modificar
data = [
[-2.273284107, 1.898485259],
[9.285248345,  9.528708054],
[-8.803332803,-1.148882298],
[4.925078368,  2.331671642],
[2.586415013,  1.28128069],
[8.084455493, -0.9130888578],
[0.9276023375, 0.5423613255],
[-7.445467699,-0.7961183742],
[-4.258454366, 9.335165888],
[1.554880819, -2.925452212]]

print("Inicializar datos :")
print(data)
print()
cd = inicializacionCentroides(data, 2)

print("Primera corrida:")
for key, value in cd.items():
    print(key)
    print(value)
    print()
print()

for i in range(3):
    nc = actualizaCentroides(cd)
    print("Nuevo Centroides:")
    print(nc)
    
    print()
    
    cd = kMeans(data, nc)
    print("Diccionario:")
    for key, value in cd.items():
        print("KEY:")
        print(key)
        print("VALUE:")
        print(value)
        print()
    print()
