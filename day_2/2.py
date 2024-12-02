#!/bin/python

import sys

def is_report_safe(n):
    safe = 1
    inc = 0
    prev = report[0]
    for x in range(1, len(report)):
        if report[x] == prev or abs(report[x] - prev) > 3:
            safe = 0
            break
        elif report[x] > prev:
            if inc == 0:
                inc = 1
            elif inc != 1:
                safe = 0
                break
        elif report[x] < prev:
            if inc == 0:
                inc = 2
            elif inc != 2:
                safe = 0
                break

        prev = report[x]

    if safe == 1:
        return True
    return False

def read_the_lines(path):
    file = open(path, 'r')
    data = file.readlines()
    file.close()

    reports = []

    for line in data:
        d = [int(x) for x in line.strip().split()]
        reports.append(d)

    return reports

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input'
reports = read_the_lines(infile)

first_part = 0
second_part = 0

for report in reports:
    is_safe = is_report_safe(report)
    if not is_safe:
        for i in range(len(report)):
            value = report[i]
            report.pop(i)
            if is_report_safe(report):
                is_safe = True
                break
            report.insert(i, value)
    else:
        first_part += 1

    if is_safe:
        second_part += 1

print(first_part)
print(second_part)

