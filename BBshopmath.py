#calculator to calculate the odds of pulling a specific item from a shop
#in backpack battles

import math

#two formulas derived by my discord, will make and test a function for both

#dkeka & luke: 

#a = % of common
#sum from 0 to 5: (5!/(k!(5-k)!)a^k(1-a)^(5-k)(k/13)

#depleted:
# p(s, i) = 0.9 * (1/s + (1 - 1/s) * p(s-1, i-1)) + 0.1 * p(s, i-1)

#after a lot of effort trevor pointed out that the formula can be simplified
#to T = r*(s/i)

rarities = [[90, 10, 0, 0, 0], 
			[84, 15, 1, 0, 0], 
			[75, 20, 5, 0, 0], 
			[64, 25, 10, 1, 0],
			[45, 35, 15, 5, 0],
			[29, 40, 20, 10, 1],
			[20, 35, 25, 15, 5],
			[20, 30, 25, 15, 10],
			[20, 28, 25, 15, 12],
			[20, 25, 25, 15, 15],
			[20, 23, 23, 17, 17],
			[20, 20, 20, 20, 20]]

print("what round is it?")
rnd = int(input())
print("what rarity item do you want?")
a = int(input())
if int(rnd) >= 12:
	 rnd = 12
	 
print(rarities[rnd-1][a])
tot = 0
slots = 5
num_items = 13
#tot = rarity * (slots/num_items)
#print(tot)
#print(rarities[0][0])

#round 1: 90/10/0/0/0
#round 2: 84/15/1/0/0
#round 3: 75/20/5/0/0
#round 4: 64/25/10/1/0
#round 5: 45/35/15/5/0
#round 6: 29/40/20/10/1
#round 7: 20/35/25/15/5
#round 8: 20/30/25/15/10
#round 9: 20/28/25/15/12
#round 10: 20/25/25/15/15
#round 11: 20/23/23/17/17
#round 12+: 20/20/20/20/20
