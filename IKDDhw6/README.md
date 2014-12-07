Homework6
========
## Require Packages
There is no need to install packages in default.

if you want to use "jaccard" in hclust or use kcaa, please install the following packages:

* install vegan
* install flexclust

if you want to evealute the result by our program, please install the following package:

* install caret (for evealute only)

## Run (command line)

    Rscript clusterAnalysis.R
    
## Evaluate    

    R CMD BATCH evealute.R

## Description
Clustering is an important means to achieve marketing segment, group identification and so on. This homework will ask you to accomplish the flow of clustering analysis. 

Please download the congressional voting data from UCI Machine Learning Repository. Please check the description of the data.

1. There are two political parties, including republican and democrat. Please remove the first column, indicating the political party, when you execute your clustering algorithm. 

2. Data attributes belong to the nominal type. Of course, you can transfer the data to "0-1" attribute and using Euclidean distance as the similarity measurement. But we encourage you to check how to measure the similarity by Jaccard distance.

3. Data contain missing values. Take care to handle missing values precisely.

Please try to make a 2-clusters result (We will execute your code to generate the result. Please specify how to run your code if you run with specific libraries).
The result of unsupervised learning clearly depends on the design of "similarity/dissimilarity" measurement. We encourage you to check how to measure the similarity by Jaccard distance. You can also try K-Mean partitioning based clustering, or check the solution of hierarchical clustering. It is also preferred to find the base code from scikits-learn (for python), Weka (for java). R also contains many good implementation of clustering algorithms. 

How to evaluate your result? We will use the attribute political party as the baseline. In fact, this data strongly reveal the effect from the political party. Their intention in these 16 issues are highly distinguishable. As such, we will evaluate your result by Confusion Matrix, and calculate your score as F1-score.

The score will depend on your F1-score, ranging from 7~10 if you finish the code and can be reproduce correctly in the TA side.

Output format: Please be complying with the output format. Please give each tuple in congressional voting data  a ID from 1~435. Your code should generate "2 files", named "cluster1.csv" and "cluster2.csv", respectively. Each file contains the IDs of all tuples belonging to the cluster -- a ID in a line.
For example, your result may like:

```
cluster1.csv
1
3
5
7
9
...
```
```
cluster2.csv
2
4
6
8 
...
```
