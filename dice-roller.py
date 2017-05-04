import random

total = 1000
current = 0
count = 0

while current < total:
    current += random.randrange(99)
    count += 1

print "Total obtenu : " + str(current)
print str(count) + " jets pour atteindre " + str(total)
