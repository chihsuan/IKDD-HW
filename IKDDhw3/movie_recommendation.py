#!/usr/bin env python
import sys
import itertools
from math import sqrt
from os.path import join, isfile, dirname

from operator import add
from pyspark.mllib.recommendation import ALS
from pyspark import SparkConf, SparkContext
from numpy import array

def parse_rating(line):
    """
    Parses a rating record in MovieLens format userId::movieId::rating::timestamp.
    """
    fields = line.strip().split("::")
    return long(fields[3]) % 10, (int(fields[0]), int(fields[1]), int(fields[2]))

def parse_movie(line):
    """
    Parses a movie record in MovieLens format movieId::movieTitle.
    """
    fields = line.strip().split("::")
    return int(fields[0]), fields[1]

def load_ratings(ratings_file):
    """
    Load ratings from file.
    """
    if not isfile(ratings_file):
        print "File %s does not exist." % ratings_file
        sys.exit(1)
    f = open(ratings_file, 'r')
    ratings = filter(lambda r: r[2] > 0, [parse_rating(line)[1] for line in f])
    f.close()
    if not ratings:
        print "No ratings provided."
        sys.exit(1)
    else:
        return ratings


if __name__=="__main__":
    if len(sys.argv) != 3:
        print sys.stderr
        exit(-1)
    
    conf = SparkConf() \
            .setAppName("MovieALS") \
            .set("spark.executor.memory", "2g")
    sc = SparkContext(conf=conf)

    # load personal ratings
    rating_data = load_ratings(sys.argv[2])
    my_rating_rdd = sc.parallelize(rating_data, 1)

    # ratings and movie titles
    movie_dir = sys.argv[1]

    ratings = sc.textFile(join(movie_dir, "ratings.dat")).map(parse_rating)
    movies = dict(sc.textFile(join(movie_dir, "movies.dat")).map(parse_movie).collect())

    rank = 8
    lmbda = 0.1
    numIter = 10
    
    training = ratings.values() \
            .union(my_rating_rdd)

    # training model
    model = ALS.train(training, rank, numIter, lmbda)
    
    # recommendation
    candidates = sc.parallelize([m for m in movies])
    y = candidates.map(lambda x: (0, x)).collect()
    predictions = model.predictAll(candidates.map(lambda x: (0, x))).collect()
    recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)[:10]
    
    f = open('output/recommendations', 'w')
    f.write("Movie recommendations:\n")
    for i in xrange(len(recommendations)):
        f.write(("%2d: %s\n" % (i+1, movies[recommendations[i][1]])).encode('ascii', 'ignore'))
    f.close()

    # clean up
    sc.stop()
