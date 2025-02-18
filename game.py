import random

random_number = random.randint(1, 15)

choice = input("Guess the number between 1 to 15")
if choice == random_number:
  print("Oh yes you win!")
else:
  print("idk")



