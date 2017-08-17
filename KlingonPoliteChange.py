#KlingonCorrectChange.py
#
#Find the polite Klingon change
#
#Victor Tang 302182945
#Ryan Ahn 301278110
#
#June 2017


#set value of each coin to its equivalent in mu value
mu = 1
shhhrok = mu
darsek = 10*mu
talon = 30*mu
lru = 90*mu


#find out cost and amount paid from user input
cost = int(input("Please enter the cost of the item: "))
paid = int(input("Please enter the amount paid: "))

#calculate change by subtracting the cost from the paid amount
change = 0 + paid - cost

#calculate the polite change
#change divided by larger coin with no remainder
#use the remainder from previous calculation to find change for subsequent coins in descending value
changeLru = change//lru
changeTalon = (change%lru)//talon
changeDarsek = ((change%lru)%talon)//darsek
changeShhhrok = (((change%lru)%talon)%darsek)//shhhrok

print ("The correct polite way to give change is: \n %i lru, \n %i talon, \n %i darsek, \n %i shhhrok." %(changeLru, changeTalon, changeDarsek, changeShhhrok))
print("--- Good-Bye ---")