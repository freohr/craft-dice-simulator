import random

total = 1000
current = 0
count = 0
rolls = []
crits = []

while current < total:
    roll = random.randrange(99)
    rolls.append(roll)
    if roll % 11 == 0:
        crits.append(roll)
        current += 2 * roll
    else:
        current += roll
    count += 1

print "Total obtenu : " + str(current)
print str(count) + " jets pour atteindre " + str(total)
print "Jets : " + str(rolls)
print "Critiques : " + str(crits)
