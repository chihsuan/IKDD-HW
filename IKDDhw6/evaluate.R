library(caret) 

truth1 <- rawData[,1]
truth1[truth1 == 'republican'] <- 1
truth1[truth1 == 'democrat'] <- 2
truth1 <- as.numeric(truth1)

truth2 <- rawData[,1]
truth2[truth2 == 'republican'] <- 2
truth2[truth2 == 'democrat'] <- 1
truth2 <- factor(as.numeric(truth2))

cp <- cbind(rawData[1], truth1)
cp <- cbind(cp, truth2)
cp <- cbind(cp, clust.kmeans)
cp <- cbind(cp, clust.hy)
cp <- cbind(cp, clust.kcca)

htable <- table(factor(clust.hy), factor(truth1))
ktable <- table(factor(clust.kmeans), factor(truth1))
ctable <- table(factor(clust.kcca), factor(truth2))
as.numeric(cp[,2]) - as.numeric(cp[,3])
as.numeric(cp[,2]) - as.numeric(cp[,4])

print(confusionMatrix(htable)$overall[1])
print(confusionMatrix(ktable)$overall[1])
print(confusionMatrix(ctable)$overall[1])

retrieved <- length(clust.kmeans)
precision <- sum(clust.hy == truth1) / retrieved
recall <- sum(clust.hy == truth1) / sum(truth1)
Fmeasure <- 2 * precision * recall / (precision + recall)
print(Fmeasure)

retrieved <- length(clust.kmeans)
precision <- sum(clust.kmeans == truth1) / retrieved
recall <- sum(clust.kmeans == truth1) / sum(truth1)
Fmeasure <- 2 * precision * recall / (precision + recall)
print(Fmeasure)
