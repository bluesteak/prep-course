#Riddle question, hint, answer - can be changed
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
riddle = "'I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?''"
text_hint = "Lighten up my way"
number_hint = "6, 9, 18, 5"
riddle_answer = "fire"
#rock-paper-scissor game
def game():
  import random
  choices = ["rock","paper","scissors"]

  cat = random.choice(choices)
  player = None
  win = "Yah! you win!"
  lose = "You lose the game!"
  while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

    if player == cat:
      print("computer: ",cat)
      print("player: ",player)
      print("Tie!")

    elif player == "rock":
      if cat == "paper":
        print("computer: ", cat)
        print("player: ", player)
        print(win)
      if cat == "scissors":
        print("computer: ", cat)
        print("player: ", player)
        print(win)

    elif player == "scissors":
      if cat == "rock":
        print("computer: ", cat)
        print("player: ", player)
        print("You lose!")
      if cat == "paper":
        print("computer: ", cat)
        print("player: ", player)
        print("You win!")

    elif player == "paper":
      if cat == "scissors":
              print("computer: ", cat)
              print("player: ", player)
              print("You lose!")
      if cat == "rock":
              print("computer: ", cat)
              print("player: ", player)
              print("You win!")

#Right Cave Function
def right_cave():
  print("You chose RIGHT cave.When you go inside, you hear a noise!")
  print("MEOW~~~~")
  print("A wild Fluffy Cat appears")
  print("      /\_____/\   ")
  print("     /  o   o  \ ~Meow. Let's play~")
  print("    ( ==  ^  == )   ")
  print("     )         (    ")
  print("    (           )   ")
  print("   ( (  )   (  ) )    ")
  print("  (__(__)___(__)__)    ")
  print("'Meow~ Let play one round of rock-paper-scissors game. If you win, I can help you solve the riddle and win the treasure.'")
  game()
  
#Left Cave Function
def left_cave():
  print("You chose LEFT cave. When you step inside, you see a sleeping 3- feet-tall Black Cat.What would you do?")
  
  print("       |\      _,,,---,,_ ") 
  print("ZZZzz /,`.-'`'    -.  ;-;;,_")
  print("     |,4-  ) )-,_. ,\ (  `'-' ")
  print("    '---''(_/--'  `-'\_)     (ಠ_ಠ) you")
  print("    ")
  print()
  print("(A) PET THE CAT")
  print("(B) SNEAK UP BEHIND IT TO ESCAPE")
  left_pick = input("Type your choose here. A or B? ")
  left_pick = left_pick.lower()
  if left_pick == "a" == "b":
    print("The giant cat wakes up and sees you. You are trapped there forever and become a toy for the cat. Sorry buddy...")
  else:
    print("No matter what you pick, the giant cat wakes up and sees you. You are now trapped here and become cat's toy. Sorry.. (not sorry.Meow~)...")

#Riddle Function
def the_riddle():
  print("       +++++++++++++++++")
  print(riddle)
  print("       +++++++++++++++++")
  print("Hint 1:",text_hint)
  print("Hint 2: when A become One - ",number_hint)
  print()
  print("What is the answer?")

#Decode Message Function:
def decode_riddle_hint():
  guesses = []
  while True:
    print("Type in each hint number - enter 'done' to exit:")
    your_choice = input("> ")
    your_choice = your_choice.lower()
    if your_choice == "done":
        break
    your_choice = int(your_choice)
    guesses.append(your_choice)

    for guess in guesses:
      print(alpha[guess-1], end='')
    print()
#Able to solve the riddle message
def solve_riddle_road():
  print("Congraduation! You have found the treasure! This is what you found inside:")
  print("___________________________________")
  print("|#######====================#######|")
  print("|#(1)*UNITED STATES OF AMERICA*(1)#|")
  print("|#**          /===\   ********  **#|")
  print("|*# {G}      | ('' |              #|")
  print("|#*  ******  | /v\ |    O N E    *#|")
  print("|#(1)         \===/            (1)#|")
  print("|##======== ONE DOLLAR ==========##|")
  print("------------------------------------")

#Start Game:
print("You are walking in the forest and see a beam light from far ahead.")
print("When you come nearby, you see a weird cat with a sparkle suit standing in front of 2 caves")
print(" /\_/\ ")
print("( o.o )")
print(" > ^ < ")

print("❁ Meoww~ ❁ What is your name?❁")
#Get user name
name = input("Enter name:")
name = name.title()
#Cat ask which door which Play choose using a riddle 
# player choose door using input
#   option A - left cave
#   option B - right cave
#

print()
print("Cat: Hi there,",name,"!")
print("Cat: Here is a riddle for you to solve.")
#Insert riddle here
the_riddle()
print("If you can answer it, you win the treasure,",name,"!")
print("If you don't know the answer, type anything to continue the game")
answer = input("Type here: ")
answer = answer.lower()

#Correct answer - win the game
if answer == riddle_answer:
  solve_riddle_road()

#Wrong answer - continue with the game
else:

  print("Cat: Sorry that is not a correct answer. It's alright,",name,". Let's continue the journey. Meow~")
  print("Please pick a cave to go inside.")
  while True:
    print("LEFT or RIGHT cave?")
    pick_cave = input("> ")
    pick_cave = pick_cave.lower()

#LEFT CAVE - Dead end cave -> die
    if pick_cave == "left":
      left_cave()
      break

#RIGHT CAVE - Correct cave 
    elif pick_cave == "right":
      right_cave()
      print("Did you win or lose the game?Type 'win' or 'lose' or 'tie':")
      game_result = input("> ").lower() 
      if game_result == "win" or game_result == "tie":
        print("Either you win or tie, Fluffy White Cat will help you solve the riddle.Please type each number by order to the Decrypt Devide.")
        print("")
        print(" _______")
        print("|.-----.|  Decrypt Devide appears! ")
        print("||     ||  Enter one number each time")
        print("||_____/|  Hint:,",number_hint)
        print("| .     |")
        print("|-|-  oo|")
        print("|  _ _  |")
        print("|_______/")
       

        decode_riddle_hint()
        print("Try to type in the correct answer!")
        the_riddle()
        answer = input("> ")
        answer = answer.lower()


        #Correct answer - win the game
        while True:
          if answer == riddle_answer:
            solve_riddle_road()
            break
        #Wrong answer - try again
          else:
            print("Decrypt Devide has given you the answer. Please try again!")
            break
      elif game_result == "lose":
        print("You lost. White Fluffy cat still helps guide you to the treasure but he takes 90% comission and you ended up with a left over slide of pizza")
        print(" // ""--.._ ")
        print("||  (_)  _  -._     ")
        print("||    _ (_)    '-.   ")
        print("||   (_)   __..-'    ")
        print(" \__..--""    ")
        
         
        break
      break

#OTHER OPTION - not valid. return to choose left or right
    else:
      print("Sorry,",name,". Our budget is low so we don't have other options. Please choose either left or right")
        
