#library(vegan)       # For vegdist 
#library(flexclust)   # For kcca

### READ Data ###
rawData <- read.csv('dataset/house-votes-84.data', stringsAsFactors=FALSE)
data <- rawData[, 2:ncol(rawData)]

### preprocessing ###
data[data == 'n'] <- 0
data[data == 'y'] <- 1
data[data == '?'] <- 0
data[, 1:ncol(data)] <- sapply(data[, 1:ncol(data)], as.numeric)

### select attr ###
data <- data[,c(4)]

#dist.mat<- vegdist(data, method="euclidean")
#clust.hy <- hclust(dist.mat)
#clust.hy <- cutree(clust.hy, k=2)
#clust.kcca <- clusters(kcca(data, k=2, family=kccaFamily("jaccard")))
clust.kmeans <-  kmeans(data, 2)[1]$cluster

clust1 <- data.frame()
clust2 <- data.frame()

for (i in 1:length(clust.kmeans)) {
  if (clust.kmeans[i] == 1) {
    clust1 <- rbind(clust1, i)
  }
  else {
    clust2 <- rbind(clust2, i)    
  }
}

write.table(clust1, 'cluster1.csv', row.names=FALSE, col.names = FALSE)
write.table(clust2, 'cluster2.csv', row.names=FALSE, col.names = FALSE)

print('success, output: cluster1.csv, cluster2.csv')
