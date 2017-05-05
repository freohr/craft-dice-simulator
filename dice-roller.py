import argparse
import random

parser = argparse.ArgumentParser(
    description="Script permettant de simuler un ensemble de jet de d100 pour atteindre un score total")

parser.add_argument("total", type=int, help="Total a atteindre")
parser.add_argument("seuil", type=int, help="Seuil de reussite du jet (jet reussi si inferieur au seuil)")

args = parser.parse_args()

total = args.total
threshold = args.seuil
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
