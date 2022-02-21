from random import randint
from sys import exit

def ghost_game():
  print("Ghost Game")
  feeling_brave = True
  score = 0
 

  while feeling_brave:
    ghost_door = randint(1, 3)
    print("Three doors ahead.")
    print("Which two are safe?")
    door = input("1, 2 or 3?")
    door_num = int(door)
    if door_num == ghost_door:
      printScore = str(score)
      print("AHHHHHHHHH... You died")
      print("Your Score was " + printScore)
      feeling_brave = False
      try_again = input(" Do you want to try again? Enter 1 for Yes, 2 for No")
      try_result = int(try_again)
      if try_result == 1:
        ghost_game()
      if try_result == 2:
        print("Thanks for playing!")
        break

    else:
      print("No Ghost!")
      print("You enter the room.")
      score = score + 1

ghost_game()
  