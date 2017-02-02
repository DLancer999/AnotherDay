#!/usr/bin/env python3
#  
# Copyright (c) Kavvadias Ioannis. All rights reserved.  
# email: kavvadiasj@hotmail.com
#

import sys
sys.path.append('src/')

from functions import *

from script import initializeScript

replayGame = True
while replayGame:
    #Start game 

    #initialize script
    allText = initializeScript()

    #start at buildingEntrance dialogue
    runningTag = findTag(allText, 'buildingEntrance')
    gameRunning = True

    #initialize flags for special events
    specialVars = specialStuff(allText)

    #input characters name
    setCharactersName(specialVars)

    #short-curcuit for test!
    #runningTag = findTag(allText, 'typicalQualifications')

    #Lets play!
    while gameRunning:
        #handle unique behaviour of running paragraph
        allText[runningTag].uniqueBehaviour(allText,specialVars)
        #show what is going on
        allText[runningTag].printText()
        #check for game ending
        gameRunning = not allText[runningTag].lastParagraph
        if not gameRunning: continue
        #show available options
        allText[runningTag].printOptions()
        #retrive next dialogue
        optionSelected = selector(allText[runningTag].nActiveOptions())-1
        actuallOptionSelected = allText[runningTag].mapToActiveOptions(optionSelected)
        nextTag = allText[runningTag].optionsTarget[actuallOptionSelected]

        #update runningTag
        runningTag = nextTag
    #GameLoop End

    #check for game restart
    replayGame = printEnding(allText, specialVars)

printTnx()
input()
#seeWholeTree(initializeScript())
    
