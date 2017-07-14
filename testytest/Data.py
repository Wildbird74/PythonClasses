import csv
import numpy

result = numpy.array(list(csv.reader(open("Sprint6.csv", "rb"), delimiter=","))).astype("float")

print(result)
