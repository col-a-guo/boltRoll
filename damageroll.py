# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:34:38 2021

@author: r2d2go
"""

import random

critRange = 4
advrolls = 3

def damageRoll(crit):
    rollList = []
    if crit == True:
        for i in range(4):
            rollList.append(random.randint(1,8))
    else:
        for i in range(2):
            rollList.append(random.randint(1,8))
    return rollList


def chaosCheck(rollList,rerollCount):
    rollTotal = 0
    ricochet = False
    twoCheck = False
    for i in range(len(rollList)):
        if rollList[i] == 2:
            twoCheck = True
        for j in range(len(rollList)):
            if rollList[i] == rollList[j]:
                if i != j: 
                    ricochet = True
    
    if twoCheck == False:
        for roll in rollList:
            if roll == 1:
                roll = 2
                twoCheck == True
                if twoCheck == True:
                    ricochet == True
                
    for roll in rollList:
        if roll == 1:
            roll = 2
            ricochet == True
    wild = False
    if ricochet == False and rerollCount == 2:
        wild = True
        rollmin = 9
        rollminI = 9
        rolledList = []
        rollrepeat = False
        rerolls = 0
        twoRoll = 9
        while rerolls < 4:
            rerolls += 1
            for i in range(len(rollList)):
                if rollmin > rollList[i]:
                    for rollC in rolledList:
                        if rollC == i:
                            rollrepeat = True
                    if rollrepeat == False:
                        rollmin = rollList[i]                
                    rollminI = i
            rollList[rollminI] = random.randint(1,8)
            rolledList.append(rollminI)
            if rollList[rollminI] == 1 or 2:
                if twoCheck == False:
                    twoCheck = True
                    twoRoll = rollminI
                elif twoRoll != 9:
                    rollList[rollminI] = 2
                    rollList[twoRoll] = 2
            for i in range(len(rollList)):
                if rollList[rollminI] == rollList[i]:
                    if i != rollminI:
                        ricochet = True
                    
                    
            if rerolls == 4:
                if twoRoll != 9:
                    rollList[twoRoll] = random.randint(1,8)
    for roll in rollList:
        rollTotal += roll
    rollTotal += random.randint(1,2)+6
    rollTotal += random.randint(1,4)+2
    return(rollTotal, ricochet, wild)
    
check = 0
ricochetCount = 0
totalDamage = 0

ricochet = True

while ricochet == True:
    crit = False
    attackRoll = 0
    rerollCount = 0
    wild = False
    totalList = []
    for i in range(advrolls):
        atk = random.randint(1,20)
        if atk > attackRoll:
            attackRoll = atk
    if attackRoll > (20-critRange):
        crit = True
    rollList = damageRoll(crit)
    rollTotal, ricochet, wild = chaosCheck(rollList,rerollCount)

    totalList.append(rollTotal)
    while (ricochet == False or rerollCount < 1) and rerollCount < 2:
        rerollCount += 1
        rollList = damageRoll(crit)
        rollTotal, ricochet, wild = chaosCheck(rollList,rerollCount)
        totalList.append(rollTotal)
    print ("ATK: "+str(attackRoll))
    print ("rerolls: "+str(rerollCount))
    print ("ricochet: "+str(ricochet))
    print ("wild: "+str(wild))
    print ("DMG: "+str(max(totalList)))
    print()
    print ('-------')
    print()
    check += 1
    totalDamage += max(totalList)
    
    if ricochet == True:
        ricochetCount+=1

print(ricochetCount)
print(totalDamage)

        
        
    
    
        
