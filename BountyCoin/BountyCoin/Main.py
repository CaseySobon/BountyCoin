#this is the program we run
#this is a script

from Chain import The_Chain #getting The_Chain from chain folder
from BountyCoin import Bounty

chain = The_Chain(10) #initial value

i = 0 #initial count


while(True):#infinite loop waiting for bounties


    Task = input("Create a bounty: ") #ask for a bount
    chain.place_bounty(Task) #add the bounty to the list
    chain.mine() #mine a new coin
    print(chain.blocks[i]) #print the coin
    
    i += 1 #increment