import sys
type = sys.argv[1]
if type == "t2.micro" :
   print("It will cost you 2 dollars")
elif type == "t2.medium" :
   print("It will cost you :around 4 dollars")
elif type == "t2.large" :
   print("It will cost you around 8 dollars")
else :
   print("Your input is invalid")   