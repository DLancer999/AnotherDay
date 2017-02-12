#  
# Copyright (c) Kavvadias Ioannis. All rights reserved.  
# email: kavvadiasj@hotmail.com
#

from copy import deepcopy
import textwrap


#for dialogues without unique behaviour
#--------------------------------#
def doesNothing(allText,specialVars):
#--------------------------------#
    pass
#functionEnd

#--------------------------------#
def endProg():
#--------------------------------#
    exit(0)
#functionEnd

#select option function
#--------------------------------#
def selector(maxValue):
#--------------------------------#
    retryMessage = '> Available Options are 1-{}'.format(maxValue)
    while True:
        #read input from keyboard
        choice = input('>  ')
        try:
            choiceValue = int(choice)
            #check if value within specified parameters
            if choiceValue > 0 and choiceValue <= maxValue:
                return choiceValue
        #input not of integer type
        except:
            pass
        print (retryMessage)
    return 0
#functionEnd

#for debugging purposes
#--------------------------------#
def seeWholeTree(allText,specialVars):
#--------------------------------#
    for text in allText:
        print ('') 
        print ('')
        print ('----> {} <----'.format(text.name))
        print ('testing unique behaviour', end=" "),
        text.uniqueBehaviour(allText,specialVars)
        print ('-OK-')
        print ('testing text and options')
        text.printText()
        if text.lastParagraph:
            print ('')
            print ('Ending Paragraph - No Options to Show')
            continue
        text.printAllOptions()
        print ('')
        print ('options target')
        for iOpt,opt in enumerate(text.options):
            print('{}--> {}'.format(iOpt+1,allText[text.optionsTarget[iOpt]].name))
        #text.optionsTarget[actuallOptionSelected]

    print ('')
    print ('')
    print ('--->Test Completed Successfuly<---')
#functionEnd

#--------------------------------#
class dialogue:
#--------------------------------#
    #constructor
    #--------------------------------#
    def __init__(self, allText, name, goToOption, returnToOption, \
        uniqueBehaviour=doesNothing):
    #--------------------------------#
        #dialogue variables decleration
        self.name = name                       #dialogue name
        self.tag = len(allText)                #dialogue tag (in registry)
        self.text           = []               #text to be printed 
        self.textName       = []               #used to set text dynamically 
        self.goToOption     = goToOption       #text for option that  leads  to this dialogue 
        self.returnToOption = returnToOption   #text for option that returns to this dialogue 
        self.optionsTarget  = []               #list of possible destinations (tags)
        self.optionsName    = []               #list of possible destinations (names)
        self.options        = []               #list of possible destinations ((go||return)ToOption Texts)
        self.isOptionActive = []               #used to dynamically activate-deactivate options
        self.lastParagraph  = False            #used to end game
        self.uniqueBehaviour = uniqueBehaviour #function pointer to handle unique behaviour (if needed)
        allText.append(self)                   #append self to dialogue registry
    #functionEnd

    #--------------------------------#
    def addText(self, text, textName="NA", newLine=False):
    #--------------------------------#
        nLines = len(self.text)
        if nLines==0 or newLine:
            self.text.append(text)
            self.textName.append(textName)
        else:
            self.text[nLines-1] += " " + text
        #formatText(self.text, 65)
    #functionEnd

    #--------------------------------#
    def printText(self):
    #--------------------------------#
        #leave two empty lines
        print ('\n')
        if len(self.text) == 0:
            print ('ERROR::printText::text for dialogue {} is not defined'.format(self.name))
            endProg()
        else:
           #for line in self.text:
           #    print (line)
            textString = ''
            for line in self.text:
                textString += line
            print(textwrap.fill(textString,70))
    #functionEnd

    #--------------------------------#
    def setGoToOption(self,option):
    #--------------------------------#
        self.goToOption = option
    #functionEnd

    #--------------------------------#
    def setReturnToOption(self,option):
    #--------------------------------#
        self.returnToOption = option
    #functionEnd

    #--------------------------------#
    def addOption(self,option, go=True, active=True):
    #--------------------------------#
        if go:
            self.options.append(option.goToOption)
        else:
            self.options.append(option.returnToOption)
        self.optionsTarget.append(option.tag)
        self.optionsName.append(option.name)
        self.isOptionActive.append(active)
    #functionEnd

    #--------------------------------#
    def findOption(self,name):
    #--------------------------------#
        for iOpt,optName in enumerate(self.optionsName):
            if name==optName:
                return iOpt
        print ('ERROR::findOption::option with name {} not found in dialogue {}'.format(name,self.name))
        endProg()
        return -1
    #functionEnd

    #--------------------------------#
    def findText(self,name):
    #--------------------------------#
        for iTxt,txtName in enumerate(self.textName):
            if name==txtName:
                return iTxt
        print ('ERROR::findText::text with name {} not found in dialogue {}'.format(name,self.name))
        endProg()
        return -1
    #functionEnd

    #--------------------------------#
    def printActiveOptions(self):
    #--------------------------------#
        if len(self.options) == 0:
            print ('ERROR::printActiveOptions::options for dialogue {} are not defined'.format(self.name))
            endProg()
        else:
            iActiveOption = 0
            print ('-------------------------------------')
            for iOption,option in enumerate(self.options):
                if self.isOptionActive[iOption]:
                    iActiveOption += 1
                    printString = str(iActiveOption)+'. '+option
                    dedented_text = textwrap.dedent(printString).strip()
                    print(textwrap.fill(dedented_text,
                        initial_indent='',
                        subsequent_indent=' ' * 3,
                        width=65,
                        ))
    #functionEnd

    #--------------------------------#
    def printAllOptions(self):
    #--------------------------------#
        if len(self.options) == 0:
            print ('ERROR::printAllOptions::options for dialogue {} are not defined'.format(self.name))
            endProg()
        else:
            iActiveOption = 0
            print ('-------------------------------------')
            for iOption,option in enumerate(self.options):
               printString = str(iOption)+'. '+option
               dedented_text = textwrap.dedent(printString).strip()
               print(textwrap.fill(dedented_text,
                   initial_indent='',
                   subsequent_indent=' ' * 3,
                   width=65,
                   ))
    #functionEnd

    #--------------------------------#
    def setOptionStatus(self,optionName,status):
    #--------------------------------#
        optionTag = self.findOption(optionName)
        self.isOptionActive[optionTag] = status
    #functionEnd

    #--------------------------------#
    def mapToActiveOptions(self,iOption):
    #--------------------------------#
        mapper = []
        for i,active in enumerate(self.isOptionActive):
            if active:
                mapper.append(i)
        return mapper[iOption]
    #functionEnd

    #--------------------------------#
    def nOptions(self):
    #--------------------------------#
        return len(self.options)
    #functionEnd

    #--------------------------------#
    def nActiveOptions(self):
    #--------------------------------#
        numberOfActiveOptions = 0
        for active in self.isOptionActive:
            if active: numberOfActiveOptions+=1
        return numberOfActiveOptions
    #functionEnd
#classEnd

#--------------------------------#
class specialStuff:
#--------------------------------#
    #constructor
    #--------------------------------#
    def __init__(self,allText):
    #--------------------------------#
        #die saga
        self.isDieMagical = False
        self.isDieTaken = False
        #drinking saga
        self.coffee   = False
        self.tea      = False
        self.hotChoco = False
        self.nothing  = False
        #eduBackground saga
        self.cfd      = False
        self.CUDAC    = False
        self.diplThes = False
        self.phdThes  = False
        self.adjoint  = False
        #ending flag
        self.goodEnding = True
        #characters name
        self.interviewersName = ''
    #functionEnd
#classEnd

#--------------------------------#
def setCharactersName(specialVars):
#--------------------------------#
    print ('Welcome to AnotherDay RPG!?')
    print ('Please enter character\'s name?')
    charName = input('>')

    #set name prefix
    titles = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Other']

    print ('Character\'s title?')
    for i,title in enumerate(titles):
        print ('{}. {}'.format(i+1,title))

    #select title
    iTitle=selector(5)
    runningTitle = ""
    if iTitle<5:
        runningTitle = titles[iTitle-1]
    else:
        print ('Please give title:')
        runningTitle = input('>')
    #short-circuit for debugging
   #charName = 'John Rambo'
   #runningTitle = 'Major'
    
    #store name
    specialVars.interviewersName = runningTitle + " " + charName
#functionEnd

#--------------------------------#
def findTag(allText, name):
#--------------------------------#
    for text in allText:
        if text.name == name:
            return text.tag
    print ('ERROR::findTag::Dialog {} not found'.format(name))
    endProg()
    return -1
#functionEnd

#--------------------------------#
def printEnding(allText, specialVars):
#--------------------------------#

    print('\n')
    if specialVars.goodEnding:
        print('---------> Good Ending <---------')
    else:
        print('---------> Bad Ending <----------')
    print('\n')
    print('Thank you for playing!!')
    print('Try again?')
    print ('-------------------------------------')
    options = ['Yes', 'No']
    for i,title in enumerate(options):
        print ('{}. {}'.format(i+1,title))
    iOpt=selector(2)
    replayGame = True
    if iOpt == 2: replayGame = False
    return replayGame
#functionEnd

#--------------------------------#
def printTnx():
#--------------------------------#
    print('')
    print('Hope you had fun!! Looking forward to hearing from you')
    print('Kavvadias Giannis')
#functionEnd

