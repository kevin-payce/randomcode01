import random
import time
import json

json_file = open("fish.txt", "r")
fish = json.load(json_file)
json_file.close()
print(fish[1]["fish_name"])
quit = 0
fish_total = 0
total_gold = 0
fish_xp = 1
bottom_fish_level = 0
rounded_fish_xp = 0



while quit == 0:
	print("[f]ish, [q]uit")
	answer = input("What would you like to do? ")
	if answer == "q":
		quit = 1
	if answer == "f":
		caught_fish = random.randint(bottom_fish_level,rounded_fish_xp)
		print(fish[caught_fish]["fish_name"])
		total_gold = total_gold + fish[caught_fish]["fish_price"]
		print(total_gold)
		fish_xp = fish_xp + 0.25
		rounded_fish_xp = round(fish_xp)
		print("Fish XP is {}. Rounded fish XP is {}", fish_xp, rounded_fish_xp)
		if rounded_fish_xp == len(fish):
			quit = 1
 

		







