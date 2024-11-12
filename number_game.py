import random
number = random.randint(1,10)
guess = None

while guess != number:
  guess = input("1 to 10")
  guess = int(guess)

  if guess == number:
   print("cong")
   break
  else:
   print("try again")
