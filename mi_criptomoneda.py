'''
Título del proyecto: Mi criptomoneda con Pyhton
Autor: Erik Urresta
'''
# Importaciones 

import hashlib
import datetime
import json 
import pprint 
from time import time

# ---------------------------- BLOQUE ---------------------------- 

class Block:
    
    # Constructor
    
    def __init__(self, timeStamp, trans, previousBlock = "" ):
        self.timeStamp = timeStamp
        self.trans = trans
        self.previousBlock = previousBlock
        self.difficultyIncrement = 0
        self.hash = self.calculateHash(trans, timeStamp, self.difficultyIncrement)
        
    # Función para calcular el hash
    
    def calculateHash(self, data, timeStamp, difficultyIncrement):
        data = str(data) + str(timeStamp) + str(difficultyIncrement)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()
    
    # Función para realizar el minado de bloques
    def mineBlock(self, difficulty):
        # Hash : 0000....023432fsdf432dsd223
        difficultyCheck = '0' * difficulty
        # Comprobamos que el hash tenga tantos ceros como indica la dificultad 
        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.trans, self.timeStamp, self.difficultyIncrement)
            self.difficultyIncrement += 1
        
# ---------------------------- CADENA DE BLOQUES ---------------------------- 

class BlockChain:
    # Constructor
    def __init__(self):
        self.chain = [self.GenesisBlock()]
        self.difficulty = 5
        self.pendingTransaction = []
        self.reward = 10
        
    # Función Bloque Genesis   
    def GenesisBlock(self):
        genesisBlock = Block(str(datetime.datetime.now()), 'Soy el bloque 0 de loa caneda de bloques')
        return genesisBlock
    
    # Conseguir el último bloque de la cadena
    def getLastBlock(self):
        return self.chain[len(self.chain)-1]
    
    def minePendingTrans(self, minerRewarsAddress):
        newBlock = Block(str(datetime.datetime.now()), self.pendingTransaction)
        newBlock.mineBlock(self.difficulty)
        newBlock.previousBlock = self.getLastBlock().hash
        
        print(f'Hash del bloque previo {newBlock.previousBlock}')
        
        testChain = []
        for trans in newBlock.trans:
            temp = json.dumps(trans.__dict__, indent=5, separators=(',',':'))
            testChain.append(temp)
        pprint.pprint(testChain)
        
        self.chain.append(newBlock)
        print(f'Hash del bloque: {newBlock.hash}')
        print('Nueo Bloque Añadido')
        
        rewardTrans = Transaction('Sistema', minerRewarsAddress, self.reward)
        self.pendingTransaction.append(rewardTrans)
        self.pendingTransaction = []
        
    def isChainValid(self):
        
        for x in range (1, len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]
            
            if (currentBlock.previousBlock != previousBlock.hash):
                print('La cadena no es valida')
        print('La cadena es valida y segura ')
        
    # Se añade la transacción a la lista de transacciones pendientes    
    def createTrans(self, transaction):
        self.pendingTransaction.append(transaction)
        
    # Comprobar cuantas monedas tiene una wallet 
    
    def getBalance(self, walletAddress):
        balance = 0
        
        for block in self.chain:
            if block.previousBlock == "":
                continue
            for transaction in block.trans:
                if transaction.fromWallet == walletAddress:
                    balance -= transaction.amount
                if transaction.toWallet == walletAddress:
                    balance += transaction.amount
        return balance
    
# ---------------------------- TRANSACCION ---------------------------- 

class Transaction:
    # Constructor
    def __init__(self, fromWallet, toWallet, amount):
        self.fromWallet = fromWallet
        self.toWallet = toWallet
        self.amount = amount 
        
# --------------------------------------------------------------------- 
# ---------------------------- ZONA DE TESTEO -------------------------
# --------------------------------------------------------------------- 
mi_crypto = BlockChain()


print('Erik empezó a minar...')

mi_crypto.createTrans(Transaction('Alejandra', 'Gabriel', 0.01))
mi_crypto.createTrans(Transaction('Patas', 'Gabriel', 100))
mi_crypto.createTrans(Transaction('Gabriel', 'Patas', 0.01))

tiempo_inicio = time()
mi_crypto.minePendingTrans('Erik')
tiempo_final = time()
print(f'Erik tardó:  {tiempo_final-tiempo_inicio} secs en minar')

print('-'*20)

print('Fabricio empezó a minar...')

mi_crypto.createTrans(Transaction('Juan', 'Luis', 0.31))
mi_crypto.createTrans(Transaction('Alba', 'Gabriel', 10))
mi_crypto.createTrans(Transaction('Patas', 'Alba', 1343))

tiempo_inicio = time()
mi_crypto.minePendingTrans('Fabricio')
tiempo_final = time()
print(f'Fabricio tardó:  {tiempo_final-tiempo_inicio} secs en minar')

print('-'*20)

print('Nuria empezó a minar...')

mi_crypto.createTrans(Transaction('David', 'Miguel', 0.001))
mi_crypto.createTrans(Transaction('Javi', 'Patas', 130))
mi_crypto.createTrans(Transaction('Alba', 'Miguel', 9999))

tiempo_inicio = time()
mi_crypto.minePendingTrans('Nuria')
tiempo_final = time()
print(f'Nuria tardó:  {tiempo_final-tiempo_inicio} secs en minar')


print('-'*20)

print('Erik tiene' + str(mi_crypto.getBalance('Erik')) + 'ErikCoins en su wallet')
print('Fabricio tiene' + str(mi_crypto.getBalance('Fabricio')) + 'ErikCoins en su wallet')
print('Nuria tiene' + str(mi_crypto.getBalance('Nuria')) + 'ErikCoins en su wallet')

    
        
    
    
        
                    
            
        
            
            
        
        
        
            
    


    


        
        

            

    
    
    
    
        

