rawData <- read.csv('dataset/house-votes-84.data', stringsAsFactors=FALSE)
data <- rawData[, 2:ncol(rawData)]

data[data == 'n'] <- 0
data[data == 'y'] <- 1
data[data == '?'] <- 0.5


dist.mat <- dist(data, method="euclidean")
clust.hy <- hclust(dist.mat)
clust.hy <- cutree(clust.hy, k=2)
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


