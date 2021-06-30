import random
import time
gold =20
hp = 100
mobhp = 50
ohp = 100
quit = 0
x = 0
xp = 0
while quit == 0:
	moblist = [{"mob":"small rat","mobhp":50,"mobhit":2},{"mob":"large rat","mobhp":75,"mobhit":5},{"mob":"queen rat","mobhp":100,"mobhit":10},{"mob":"prison guard ","mobhp":125,"mobhit":10},{"mob":"yard warden","mobhp":125,"mobhit":15},{"mob":"bridge troll","mobhp":300,"mobhit":30},{"mob":"The Boss","mobhp":500,"mobhit":50},{"mob":"King","mobhp":1000,"mobhit":50}]
	selector = round(xp)
	mobnumber = random.randint(0,selector)
	mobname = moblist[mobnumber]['mob']
	mobhp =  moblist[mobnumber]['mobhp']
	print(mobname)
	print(" f = fight, s = shop ")
	state = input("What would you like to do?  ")
	if state == "f":
		while hp > 0 and mobhp > 0:
			hita = random.randint(0,9)
			hitb = random.randint(0,9)
			time.sleep(2)
			print(f"HP is {hp}") 
			print(f"I got hit by {hita}")
			print(f"monsters HP is {mobhp}")
			print(f"I hit the monster for {hitb}")
			hp = hp - hita
			mobhp = mobhp - hitb
			gold = gold / 2
	if hp <= 0 and mobhp > 0:
		ohp = ohp +1
		hp = ohp
		print(f"You have died, your HP is now {hp}")
		if (xp > 1):
			print("Lost 0.5 HP")
			xp = xp - 0.5
		

	if mobhp <= 0:
		gold = gold +10
		print("You killed the Monster!")
		xp = xp + 0.25
		ohp = ohp +1
		hp = ohp

	if state == "q":
		quit =1


