#the chain of the block chain
#this is the linked list

import hashlib
from BountyCoin import Bounty #taking the bounty information from the BountyCoin file


#introducing the blocks
class The_Chain():#new class the chain


    def __init__(Coin, diff): #initializing the Coin lists
        Coin.diff = diff
        Coin.blocks = []
        Coin.pool = []
        Coin.first_block()


    def test_hash(Coin, block): #how to check the hash is correct
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256-Coin.diff) and block.last_hash == Coin.blocks[-1].hash
        

    def link_block(Coin, block): #link it to the block
        if Coin.test_hash(block):
           Coin.blocks.append(block)
            

    def place_bounty(Coin, Task): #we apend the ledger with a new bounty
        Coin.pool.append(Task)
        

    def first_block(Coin):
        first_hash = hashlib.sha256()
        first_hash.update(''.encode('utf-8'))
        first = Bounty("*\nThere is no previous\n", first_hash)
        first.mine(Coin.diff)
        Coin.blocks.append(first)
        

    def mine(Coin):#mine a bountycoin from the task pool
        if len(Coin.pool) > 0:
            Task = Coin.pool.pop()
            block = Bounty(Task, Coin.blocks[-1].hash)
            block.mine(Coin.diff)
            Coin.link_block(block)