bag=["Apple"]
#this is what is in your bag

money = 20
#this is how much money you have

print("Welcome to Paddy's fruit and veg store")

print("You have " + str(bag) + " in your bag")

print("You have " + str(money) + "€ in your pocket")

while True:

    print("You can buy a banana for 1€ ")
    
    print("A dragonfruit for 9€")
    
    print("Or a bag of potatoes for 7€")
    
    buy=input("So what do you want to buy? banana, dragonfruit or bag of potatoes: ")
    #this is what you choose to buy
    
    if buy== "banana":
        bag.append("banana")
        #this adds the banana to your bag
        print("Here is your banana. It costs 1€")
        money = money - 1
        #this is how much money you spend

    elif buy== "dragonfruit":
        bag.append("dragonfruit")
        #this adds the dragonfruit to your bag
        print("Here is your dragonfruit. It costs 9€")
        money = money - 9
        #this is how much money you spend
    
    elif buy== "bag of potatoes":
        bag.append("bag of potatoes")
        #this adds the bag of potatoes into your bag
        print("Here is your bag of potatoes. It costs 7€")
        money = money - 7
        #this takes away your money that you have spent
      
    else:        
        print("Sorry we dont sell " + str(buy) + " here please go and check a phone shop")
        
    print("Thank you for visiting Paddy's store")
        
    print("You now have " +  str(bag) + " in your bag")
    #this shows you what you have in your bag
        
    print("You have " + str(money) + "€ left")
    #this shows you how much money you have left
