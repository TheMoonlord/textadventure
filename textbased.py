print("DISCLAIMER: This game has no historical accuracy")
missileShoot = input ("You are being attacked. The other plane is shooting at you and you have two choices. Do you accelerate or maneuver: ")
missileShoot = missileShoot.lower()
if missileShoot == "accelerate":
   print("The plane still shoots you and takes out both engines. Your plane falls hundreds of feet down before crashing. You died...")
   exit()
elif missileShoot == "maneuver":
   dive = input("You perform a barrel roll, and the plane misses. \nBut now the plane is aimed to crash into you.\nDive or climb: ")
   dive = dive.lower()
else:
   print("Sorry, I didn't get that.")
   exit()

if dive == "dive":
   print("Your plane dives directly into the gasoline storage of the other plane, and both explode spectacularly. You died...")
   exit()
elif dive == "climb":
   fireOrDive = input("You climb into the air. The plane misses you by a foot, and you watch as it crashes straight into another. \nHowever, two more planes rise to face you. \nFire or dive: ")
   fireOrDive = fireOrDive.lower()
else:
   print("Sorry, I didn't get that.")
   exit()

if fireOrDive == "fire":
   print("You miss, and they fire back. \nIt hits your gasoline storage and your plane explodes. You died...")
   exit()
elif fireOrDive == "dive":
   fireOrAccel = input("You dive between them, and they both fire at each other, falling out of the sky. \nNow a huge plane appears. It hasn't seen you yet. \nFire or accelerate: ")
   fireOrAccel = fireOrAccel.lower()
else:
   print("Sorry, I didn't get that.")
   exit()

if fireOrAccel == "accelerate":
   print("You get closer, but now it can see you. \nIt fires a huge missile and your plane is blown to pieces. You died...")
   exit()
elif fireOrAccel == "fire":
   accelOrRise = input("You fire at the enemy plane, and it wounds the plane, bullet holes in its side. \nNow you have its attention. \nAccelerate or climb: ")
   accelOrRise = accelOrRise.lower()
else:
   print("Sorry, I didn't get that.")
   exit()

if accelOrRise == "climb":
   print("You climb, but you are still in the plane's sight. \nIt shoots you, and you go down. You died...")
   exit()
elif accelOrRise == "accelerate":
   diveOrFire = input("You are at the front of the other plane now. None of the turrets can reach you. \nDive or fire: ")
else:
   print("Sorry, I didn't get that.")
   exit()

if diveOrFire == "dive":
   print("You dive, but now you are exposed to the lower turret. \nThe turret fires at your wing and it snaps off, making you fall. You died...")
   exit()
elif diveOrFire == "fire":
   print("The plane shakes and goes down, exploding in flames. \nYou are on your guard, but there are no other planes to be found. \nYou have defeated them all. You win.")
else:
   print("Sorry, I didn't get that.")
   exit()
