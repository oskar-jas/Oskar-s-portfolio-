
while True:

	from time import sleep
	import sound #this only works in pythonista

	def easy():
	  score = 0
	  print("")
	  answer=input("Your letters are: N,P,E :")

	  if answer=="PEN":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="NEP":
	    print("WRONG!")
	    sound.play_effect('game:Error')
	
	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")

	  answer=input("Your letters are: H,G,U :")

	  if answer=="HUG":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="GUH":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")

	  answer=input("Your letters are: U,R,O,F :")

	  if answer=="FOUR": 
	    print("CORRECT!") 
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="OURF":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')
  
	  print("")	
  
	  answer=input("Your letters are: E,D,R :")
  
	  if answer=="RED":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="ERD":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: O,R,U :")

	  if answer=="OUR":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="ROU":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: G,B,A :")

	  if answer=="BAG":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
    
	  elif answer=="GAB":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
  	
	  print("")
  	
	  answer=input("Your letters are: I,B,N :")
  
	  if answer=="BIN":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  	
	  elif answer=="NIB":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  	
	  else:
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  	
	  print("")
  	
	  answer=input("Your letters are: E,Y,S :")
  
	  if answer=="YES":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  	
	  elif answer=="EYS":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  	
	  else:
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
	  	
	  print("")
	
	  answer=input("Your letters are: S,E,U :")

	  if answer=="USE":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="UES":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
	  
	  answer=input("Your letters are: Y,T,O :")

	  if answer=="TOY":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="YOT":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')
    
	  print("")

	  print("You have " + str(score) + " point/s")
  
	def medium():
	  score = 0
	  print("")
	  answer=input("Your letters are: R,W,D,O :")

	  if answer=="WORD":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="DORW":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: K,D,C,E :")

	  if answer=="DECK":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="CKED":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: M,A,R,S,T :")

	  if answer=="SMART":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="RASTM":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: H,S,O,U,E :")

	  if answer=="HOUSE":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="SOUHE":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")
  
	  answer=input("Your letters are: D,C,O,E :")

	  if answer=="CODE":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="DOCE":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: S,P,T,E,A :")

	  if answer=="PASTE":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="TASEP":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: R,O,R,E,R :")

	  if answer=="ERROR":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
	  
	  elif answer=="RORRE":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: H,R,E,T,A :")

	  if answer=="HEART":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="TREAH":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: L,N,E,I :")

	  if answer=="LINE":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="NILE":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  answer=input("Your letters are: R,T,U,N,R,E :")

	  if answer=="RETURN":
	  	print("CORRECT!")
	  	score = score +1
	  	sound.play_effect('game:Ding_3')
  
	  elif answer=="TUNRER":
	  	print("WRONG!")
	  	sound.play_effect('game:Error')
  
	  else:
	  	print('WRONG!')
	  	sound.play_effect('game:Error')
	
	  print("")

	  print("You have " + str(score) + " point/s")
  
	def hard():
	  score = 0  

	  answer=input("Your letters are: P,H,A,L,T,B,A,E")

	  if answer=="ALPHABET":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="ALPAHBET":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: C,A,R,S,L,B,M,E")

	  if answer=="SCRAMBLE":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="SCARMBLE":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: H,S,Y,C,P,I,S")

	  if answer=="PHYSICS":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="PHSYCIS":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: P,C,I,E,T,H,Y,R,O")
    
	  if answer=="HYPOCRITE":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="HYPCORITE":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: H,C,E,R,E,A,T")

	  if answer=="TEACHER":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="TEAHCER":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: I,T,L,A,E,R,I,O,N,T,A,L")

	  if answer=="ALLITERATION":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="ALLTIERATION":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: T,I,A,O,R,R,A,D")

	  if answer=="RADIATOR":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="RADITOR":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: E,C,E,L,X,L,N,T,E")

	  if answer=="EXCELLENT":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="ECXELLENT":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: P,O,H,N,E,E,L,T,E")

	  if answer=="TELEPHONE":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="TELPEHONE":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("")
  
	  answer=input("Your letters are: S,D,I,E,U,T,O")

	  if answer=="OUTSIDE":
	    print("CORRECT!")
	    score = score +1
	    sound.play_effect('game:Ding_3')

	  elif answer=="UOTSIDE":
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  else:
	    print("WRONG!")
	    sound.play_effect('game:Error')

	  print("You have " + str(score) + " point/s")
  
	print("WELCOME TO....")
	sleep(2)
	print(" _    _  _________________ ")
	print("| |  | ||  _  | ___ |  _  |")
	print("| |  | || | | | |_/ / | | |")
	print("| |/\| || | | |    /| | | |")
	print("\  /\  /\ \_/ / |\ \| |/ / ")
	print(" \/  \/  \___/\_| \_|___/  ")
	print(" ")
	print(" _____ _____ ______  ___  ___  _________ _      ____  ")
	print("/  ___/  __ \| ___ \/ _ \ |  \/  || ___ \ |    |  __| ")
	print("\ `--.| /  \/| |_/ / /_\ \| .  . || |_/ / |    | |__  ")
	print(" `--. \ |    |    /|  _  || |\/| || ___ \ |    |  __| ")
	print("/\__/ / \__/\| |\ \| | | || |  | || |_/ / |____| |___ ")
	print("\____/ \____/\_| \_\_| |_/\_|  |_/\____/\_____/\____/ ")
	print("")
	print("")
	print("")
	sleep(2)
	print("      ___           ___           ___       ___           ___     ")
	print("     /\  \         /\__\         /\__\     /\  \         /\  \    ")
	print("    /::\  \       /:/  /        /:/  /    /::\  \       /::\  \   ")
	print("   /:/\:\  \     /:/  /        /:/  /    /:/\:\  \     /:/\ \  \  ")
	print("  /::\ \:\  \   /:/  /  ___   /:/  /    /::\ \:\  \   _\:\ \ \  \ ")
	print(" /:/\:\ \:\__\ /:/__/  /\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__)")
	print(" \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\ \:\ \/__/ \:\ \:\ \/__/")
	print("    |:|::/  /   \:\  /:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\  ")
	print("    |:|\/__/     \:\/:/  /     \:\  \    \:\ \/__/     \:\/:/  /  ")
	print("    |:|  |        \::/  /       \:\__\    \:\__\        \::/  /   ")
	print("     \|__|         \/__/         \/__/     \/__/         \/__/    ")
	print("")
	sleep(1)
	print("Make a word out of the letters given")
	sleep(2)
	print("")
	print("You MUST use all of the letters given")
	sleep(2)
	print("")
	print("If you make the correct word you will be awarded one point and will move on")
	sleep(2)
	print("")
	print("If you get it wrong you will still move onto the next question")
	sleep(2)
	print("")
	print("You MUST answer using CAPITAL LETTERS")
	sleep(2)
	print("")
	print("Choose your difficulty")
	sleep(2)
	print("")

	diff=input("Easy, Medium, Hard ")

	if diff=="EASY":
	  print("You chose EASY")
	  easy()

	elif diff=="MEDIUM":
	  print("You chose MEDIUM")
	  medium()
  
	elif diff=="HARD":
	  print("You chose HARD")
	  hard()
