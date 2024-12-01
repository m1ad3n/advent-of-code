#!/bin/python

import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input'
file = open(infile, 'r')
data = file.readlines()
file.close()

firstlist = []
secondlist = []

for line in data:
    d = line.strip().split()
    firstlist.append(int(d[0]))
    secondlist.append(int(d[1]))

firstlist.sort()
secondlist.sort()

sum = 0
for x in firstlist:
    sum += x * secondlist.count(x)

print(sum)

