import sys
from pyspark import SparkContext


if __name__=="__main__":
    if len(sys.argv) != 2:
        print sys.stderr
        exit(-1)
    sc = SparkContext()
    content =  sc.textFile(sys.argv[1])
    counts = content.flatMap(lambda line: line.split(" ")) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b)

    total = len(counts.collect())
    with open("output/wordCountResult", "w") as output:
        output.write(str(total))
    sc.stop()
