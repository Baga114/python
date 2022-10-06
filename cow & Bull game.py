gusess = 1
print("welcome to the cows and bulls games")
print("guses four digit number from 0000 to 5000 & you have 9 gusess only")
while(gusess <=9):
 user = int(input("entre your gusess of four digit number:  "))
 print(gusess, "no of gusses you took")
 print(9-gusess, " no of gusess left")
 gusess = gusess + 1
 d = str(user)
 if d !=4:
  print("only 4 digit")
  
 if gusess>9:
  print("you crossed the limit ! game over")
  break
 if user==4444:
  print("you have a cow! you won the game: ")
  break
 elif user==2222:
  print("opps you unclock bulls you loss the game")
  break
 elif user < 2000:
  print("you are fair away to reach to meet the number")
 elif user>5000:
  print("you are going outside the game range: ")