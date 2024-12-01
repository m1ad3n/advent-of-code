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
for i in range(len(firstlist)):
    sum += abs(firstlist[i] - secondlist[i])

print(sum)

