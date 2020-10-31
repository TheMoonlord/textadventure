#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
missileShoot = input ("accelerate or maneuver: ")
missileShoot = missileShoot.lower()
if missileShoot == "accelerate":
   print("the plane still shoots you and takes out both engines. your plane falls hundreds of feet down before crashing. you died...")
   exit()
elif missileShoot == "maneuver":
   dive = input("you perform a barrel roll, and the plane misses. \nbut now the plane is aimed to crash into you.\ndive or climb: ")
   dive = dive.lower()
else:
   print("sorry, I didn't get that.")
   exit()

if dive == "dive":
   print("your plane dives directly into the gasoline storage of the other plane, and both explode spectacularly. you died...")
   exit()
elif dive == "climb":
   fireOrDive = input("you climb into the air. the plane misses you by a foot, and you watch as it crashes straight into another. \nhowever, two more planes rise to face you. \nfire or dive: ")
   fireOrDive = fireOrDive.lower()
else:
   print("sorry, I didn't get that.")
   exit()

if fireOrDive == "fire":
   print("you miss, and they fire back. \nit hits your gasoline storage and your plane explodes. you died...")
   exit()
elif fireOrDive == "dive":
   fireOrAccel = input("you dive between them, and they both fire at each other, falling out of the sky. \nnow a huge plane appears. it hasn't seen you yet. \nfire or accelerate: ")
   fireOrAccel = fireOrAccel.lower()
else:
   print("sorry, I didn't get that.")
   exit()

if fireOrAccel == "accelerate":
   print("you get closer, but now it can see you. \nit fires a huge missile and your plane is blown to pieces. you died...")
   exit()
elif fireOrAccel == "fire":
   accelOrRise = input("you fire at the enemy plane, and it wounds the plane, bullet holes in its side. \nnow you have its attention. \naccelerate or climb: ")
   accelOrRise = accelOrRise.lower()
else:
   print("sorry, I didn't get that.")
   exit()

if accelOrRise == "climb":
   print("you climb, but you are still in the plane's sight. \nit shoots you, and you go down. you died...")
   exit()
elif accelOrRise == "accelerate":
   diveOrFire = input("you are at the front of the other plane now. none of the turrets can reach you. \ndive or fire: ")
else:
   print("sorry, I didn't get that.")
   exit()

if diveOrFire == "dive":
   print("you dive, but now you are exposed to the lower turret. \nthe turret fires at your wing and it snaps off, making you fall. you died...")
   exit()
elif diveOrFire == "fire":
   print("the plane shakes and goes down, exploding in flames. \nyou are on your guard, but there are no other planes to be found. \nyou have defeated them all. you win.")
else:
   print("sorry, I didn't get that.")
   exit()
