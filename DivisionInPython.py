# '/' operator is integer division means the result is integer is inputs are
# integer
# It works fine if inputs are floating point numbers.
# But if you want a float division using '/' then import 'division' from
# 'future'
# Calculate total meal cost from meal cost, tip and tax applied.

from __future__ import division

#All inputs
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

# This was to be done if we did not import division for tipPercent/100, because
# it gives wrong results.
tip = (tipPercent*0.01)*mealCost

# Since if we have imported, we can use / for floating division.
tax = (taxPercent/100)*mealCost

# round() is used to round to nearest floating point.
# int() to convert floating point to int.
totalCost = int(round(mealCost + tip + tax))

print "The total meal cost is",totalCost, "dollars."

