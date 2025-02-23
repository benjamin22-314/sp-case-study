"""
Observing the sky for a duration of 3 minutes yields a 60% probability of spotting a plane. Your
assignment is to calculate and explain the probability of spotting a plane within 1 minute based on
this observation. Provide a detailed solution outlining the reasoning behind your calculations.

Consider 1 minute to be the most distrete unit of time. 
Event(see at least one plane in a minute) = A
Event(don't see any planes in a minute) = B
P(A) = p
P(B) = 1-p

The probability of seeing at least one plane in 3 minutes is the sum of the probabilities of these events;
ABB
BAB
BBA

BAA
ABA
AAB

AAA

The probability of seeing at least one plane in 3 minutes is also equal to 1 minus the the probability 
of seeing no planes in 3 minutes. Event BBB

Prob(seeing a plane in 3 minutes) = 1 - (1-p)^3

setting 1 - (1-p)^3 = 0.6 and solve for p

p = 1 - (0.4)^(1/3) = 0.26319370027
"""

# test

import numpy as np

p = 0.26319370027
size = 50000
minute_events = np.random.binomial(n=1, p=p, size=size)

print(f"First 10 events (1 is see plane, 0 is not see plane): {minute_events[:10]}")
print(f"Proportion of 1s: {np.mean(minute_events)}")

# spotting a plane in a three minute interval
plane_spot = []
for i in range(len(minute_events)-3):
    plane_spot.append(
        1 if minute_events[i:i+3].sum()>0 else 0
    )
print(f"Chance of spotting a plane in a 3 minute interval: {np.mean(plane_spot)}")

# First 10 samples: [0 0 1 0 0 0 0 1 0 0]
# Proportion of 1s: 0.26114
# Chance of spotting a plane in a 3 minute interval: 0.5978558713522811

