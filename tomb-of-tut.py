pressTheButton = input("You are an adventurer looking for riches. \nYou've been told that there is an abundance of wealth in a tomb in the faraway land of Egypt. Tutankahman, the pharaoh's tomb. \nBut it is also said to be cursed, and anyone brave enough to rob it will have something horrifying happen to them. \nYou've already made the decision to go in... it's too late to turn back now. \nYou stay careful not to light your map instead of your torch. \nThe dim light of the torch reveals strange hieroglyphs on the walls. One almost looks like a button... do you want to press it? (Y/n) ")
pressTheButton = pressTheButton.lower()
if pressTheButton == "y":
  print("The wall cracks with the force of your press, and crumbles. You are buried under an avalanche of debris, and you die.")
  exit()
elif pressTheButton == "n":
  moveOrStay = input("You turn away, and choose to look at other things. Like... the carvings of snakes. \nOne of the people had told you the snakes were supposed to be beings to greet you in the afterlife. Keep going on, or stay where you are? (Move/stay) ")
  moveOrStay = moveOrStay.lower()
else:
  print("Not a valid answer.")
  exit()
if moveOrStay == "stay":
  leftOrRight = input("The ground crumbles beneath you, and you fall into another room. \nThis one has more carvings of the Egyptian gods you had been told of. Anubis, Osiris, and others in magestic murals spanning the length of the wall. \nYou notice the floor has something on it, but you decide it's nothing. Move left, or move right? (left/right) ")
  leftOrRight = leftOrRight.lower()
  if leftOrRight == "pickup":
    runOrExplore = input("You lean over to examine what's on the ground... and you are shocked to have your torch reveal shiny baubles made of gold and assorted gemstones, some with hieroglyphs engraved on them. \nMost likely a different tomb robber's mistakes on the way out. Now it's just a question of what to do next... (run/explore) ")
    runOrExplore = runOrExplore.lower()
    if runOrExplore == "run":
      print("In your glee-fueled excitement, you bolt to find an exit... and hear the ceiling crash down upon you. It squishes you flat, and you die.")
      exit()
    if runOrExplore == "explore":
      print("You explore for a few moments, and you find a hastily made exit, most likely made by other intruders. \nIt leads to the original chambers, and you find your way out to the open air. \nEnding: Scavenger")
      exit()
    else:
      print("Not a valid answer.")
      exit()
  elif leftOrRight == "left":
    print("You foolishly ignore the spiderweb cracks on the wall as you examine it... the wall caves in upon you, and you die.")
    exit()
  elif leftOrRight == "right":
    moveOrScan = input("You turn to the right and walk on. The light of your torch is dwindling and you need to squint to see. /nMove forward, or scan the area? (move/scan.) ")
    moveOrScan = moveOrScan.lower()
    if moveOrScan == "scan":
      print("As you scan the area, you bump into a part of the wall that is ominously tipping. \nIt shivers and detaches from the rest of the walls, smashing you, and you die.")
      exit()
    elif moveOrScan == "move":
      print("You move forward, and you hear a crack coming from the ceiling. \nYou bolt out of there, fueling your body to the brim with adrenaline, jumping to the hole, and somehow managing to find your way out. You didn't gain anything... except the knowledge that these places aren't that cursed, they just have withered over the years. \nEnding: Still Poor")
      exit()
  else:
    print("Not a valid answer.")
    exit()
elif moveOrStay == "move":
  examineOrMove = input("You move forward to search for the tomb. There are various carvings on the walls, telling the tales of death and the gods who rule it. \nExamine the carvings, or move on? (examine/move) ")
  examineOrMove = examineOrMove.lower()
  if examineOrMove == "examine":
    print("As you stare at the carvings on the wall, the ground crumbles underneath you, sending you to your death.")
    exit()
  elif examineOrMove == "move":
    walkOrRun = input("You keep moving forward until you get to what seems to be the tomb. The passageway to it is only half open- the other robbers must have left it that way. \nLuckily it isn't hard to get it all the way open. Inside, it is magnificent. Trinkets and relics of a past life, all decorated with gemstones and made of gold shine in the torchlight. \nThere was food prepared for a hungry pharaoh's soul to eat, and some pets had been taken on the journey to the afterlife. \nRun in and collect the items quickly, or walk in quietly and grab them? (run/walk) ")
    walkOrRun = walkOrRun.lower()
    if walkOrRun == "run":
      print("You sprint into the room, eager to haul the goodies out, when suddenly it crashes down on top of you, and you die.")
      exit()
    elif walkOrRun == "walk":
      print("You walk into the room calmly, and take each of the heavy items out, one by one. You have finally found the treasures said to be in Tutankhaman's tomb, and taken them. Ending: Jackpot")
      exit()
    else:
      print("Not a valid answer.")
      exit()
  else:
    print("Not a valid answer.")
    exit()
else:
  print("Not a valid answer.")
  exit()
