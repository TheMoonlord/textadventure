print("You are an adventurer looking for riches. \nYou've been told that there is an abundance of wealth in a tomb in the faraway land of Egypt. Tutankahman, the pharaoh's tomb. \nBut it is also said to be cursed, and anyone brave enough to rob it will have something horrifying happen to them. \nYou've already made the decision to go in... it's too late to turn back now.")
pressTheButton = input("There are strange hieroglyphs on the walls. One almost looks like a button... do you want to press it? (Y/n)")
pressTheButton = pressTheButton.lower
if pressTheButton == "y":
  print("The wall cracks with the force of your press, and crumbles. You are buried under an avalanche of debris, and you die.")
  exit()
elif pressTheButton == "n":
  snakeMoveOrStay = input("You turn away and choose to look at other things. Like... the carvings of snakes. \nOne of the people had told you the snakes were beings to greet you in the afterlife. Keep going on, or stay where you are? (Move/stay)")
  snakeMoveOrStay = snakeMoveOrStay.lower
else:
  print("Not a valid answer.")
if snakeMoveOrstay == "stay":
  input("The groynd crumbles")
