__author__ = 'Abhineet Saxena'

inFile = open('ilpd_normalized_data.csv', 'r')
count1, count2 = 0, 0
for line in inFile:
    line = [float(elem) for elem in line.strip().split(',')]
    if line[10] == 1.0:
        count1 += 1
    else:
        count2 += 1

print count1, count2
