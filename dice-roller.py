import random

total = 1000
threshold = 50
current = 0
count = 0
rolls = []
crits = []
bad_rolls = []
bad_crits = []

while current < total:
    roll = random.randrange(99)
    rolls.append(roll)
    if roll < threshold:
        if roll == 0:
            crits.append(roll)
            current += 2 * threshold
        if roll % 11 == 0:
            crits.append(roll)
            current += 2 * roll
        else:
            current += roll
    else:
        if roll % 11 == 0:
            bad_crits.append(roll)
        bad_rolls.append(roll)
    count += 1

print "Total obtenu : " + str(current)
print str(count) + " jets pour atteindre " + str(total)
print "Jets : " + str(rolls)
print "Critiques : " + str(crits)
print "Jets invalides : " + str(bad_rolls)
print "Critiques invalides : " + str(bad_crits)
