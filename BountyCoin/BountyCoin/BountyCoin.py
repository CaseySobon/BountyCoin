#this is where we define the block
#it acts like a node on the list


import hashlib#hash library from python

#introducing Coin 
class Bounty():#declare the new class of Bounty which it the coin
    def __init__(Coin, Task, last_hash): #Initalize the bounty and all the variables
        Coin.hash = hashlib.sha256()
        Coin.last_hash=last_hash
        Coin.iter=0
        Coin.Task=Task
 
        
    def mine(Coin, diff): #define the hash check for mining
        Coin.hash.update(str(Coin).encode('utf-8'))
        while int(Coin.hash.hexdigest(), 16) > 2**(256-diff):#if more difficult than max minus the diff level
            Coin.iter+=1 #increment the count
            Coin.hash=hashlib.sha256() #get new hash
            Coin.hash.update(str(Coin).encode('utf-8')) #update the hash

        
    def __str__(Coin): #making a string of the information to be used
        return "{}{}{}".format(Coin.last_hash.hexdigest(), Coin.Task, Coin.iter)
        