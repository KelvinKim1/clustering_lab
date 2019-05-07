import clusters

docs,words,data=clusters.readfile('dataset_vectors.txt')

num_clusters=6
print('Searching for {} clusters:'.format(num_clusters))
print()
clust=clusters.kcluster(data,distance=clusters.pearson,k=num_clusters)
print ('clusters by pearson correlation')
cluster = []
for i in range(num_clusters):
    print ('cluster {}:'.format(i+1))
    list = [docs[r] for r in clust[i]]
    cluster.append(list)
    print (list)
clusters.clust_to_csv(cluster,'pearson')

print()
clust=clusters.kcluster(data,distance=clusters.tanimoto,k=num_clusters)
print ('clusters by tanimoto coefficient')
cluster = []
for i in range(num_clusters):
    print ('cluster {}:'.format(i+1))
    list = [docs[r] for r in clust[i]]
    cluster.append(list)
    print (list)
clusters.clust_to_csv(cluster,'tanimoto')

print()
clust=clusters.kcluster(data,distance=clusters.euclidean,k=num_clusters)
print ('clusters by euclidean distance')
cluster = []
for i in range(num_clusters):
    print ('cluster {}:'.format(i+1))
    list = [docs[r] for r in clust[i]]
    cluster.append(list)
    print (list)
clusters.clust_to_csv(cluster,'euclidean')

print()
clust=clusters.kcluster(data,distance=clusters.cosine,k=num_clusters)
print ('clusters by cosine distance')
cluster = []
for i in range(num_clusters):
    print ('cluster {}:'.format(i+1))
    list = [docs[r] for r in clust[i]]
    cluster.append(list)
    print (list)
clusters.clust_to_csv(cluster,'cosine')

clust=clusters.bisectkcluster(data,distance=clusters.cosine,k=num_clusters)
print ('bisect clusters by euclidean distance')
cluster = []
for i in range(num_clusters):
    print ('cluster {}:'.format(i+1))
    list = [docs[r] for r in clust[i]]
    cluster.append(list)
    print (list)
clusters.clust_to_csv(cluster,'bisect')

'''
clusters.descriptive_label(data,clust)

clust=clusters.hcluster(data,distance=clusters.pearson)
print ('clusters by pearson correlation')
clusters.printhclust(clust,labels=docs)
clusters.drawdendrogram(clust,docs,jpeg='docsclust_pearson.jpg')

clust=clusters.hcluster(data,distance=clusters.tanimoto)
print ('clusters by tanimoto coefficient')
clusters.printhclust(clust,labels=docs)
clusters.drawdendrogram(clust,docs,jpeg='docsclust_tanimoto.jpg')

clust=clusters.hcluster(data,distance=clusters.euclidean)
print ('clusters by euclidean distance')
clusters.printhclust(clust,labels=docs)
clusters.drawdendrogram(clust,docs,jpeg='docsclust_euclidean.jpg')

clust=clusters.hcluster(data,distance=clusters.cosine)
print ('clusters by euclidean distance')
clusters.printhclust(clust,labels=docs)
clusters.drawdendrogram(clust,docs,jpeg='docsclust_cosine.jpg')

'''