#rock_paper_scissor
import random
  
def play():
  user = input("enter your sign'r','p','s':")
  computer = random.choice(['r','p','s']) 
    
  if user == computer:
    return "tie"
 
  if is_win(user, computer):
    return "you win"

  return "you lose"
  
def is_win(user,oppo):
  if (user == 'r' and oppo == 's') or (user == 'p' and oppo == 'r') or (user == 's' and oppo == 'p'):
    return True

print(play())
