Spark_HW
========
## Requirement
+ install Java & Scala
+ export JAVA_HOME & SCALA_HOME

## install Spark 
1. go to https://spark.apache.org/
2. download and unzip it 
3. go into the top-level Spark directory and run <code> sbt/sbt assembly </code>
4. export SPARK_HOME
5. run <code>./sbin/start-all.sh or ./bin/spark-shell </code>

## Word Count
+ Data : http://www.gutenberg.org/ebooks/5000
+ Output: total word number

## Movie Recommendation
+ Trainning Data : http://arbor.ee.ntu.edu.tw/~wisely/data/lesson.tgz
+ Input: 10 rating(1-5) on the 10 movie
+ Output: Top 10 recommendation movie 
