#  
# Copyright (c) Kavvadias Ioannis. All rights reserved.  
# email: kavvadiasj@hotmail.com
#

from functions import *

#--------------------------------#
def actionApartmentDoor(allText,specialVars):
#--------------------------------#
    doorTag = findTag(allText, 'apartmentDoor')
    interNameTag = allText[doorTag].findText('INTERVIEWERSNAME')
    allText[doorTag].text[interNameTag] = specialVars.interviewersName
#functionEnd

#--------------------------------#
def actionIdentifyDie(allText,specialVars):
#--------------------------------#
    specialVars.isDieMagical = True

    deskTag = findTag(allText,'desk')
    #activate options
    active = True
    allText[deskTag].setOptionStatus('rerollDieFinal', active)
    allText[deskTag].setOptionStatus(    'takeDie',    active)
    #deactivate options
    notActive = False
    allText[deskTag].setOptionStatus('rollDie', notActive)
#functionEnd

#--------------------------------#
def actionTakeDie(allText,specialVars):
#--------------------------------#
    specialVars.isDieTaken = True
    
    deskTag = findTag(allText,'desk')
    #activate options
    active = True
    allText[deskTag].setOptionStatus('putDieBack',    active)
    #deactivate options
    notActive = False
    allText[deskTag].setOptionStatus(   'takeDie'    , notActive)
    allText[deskTag].setOptionStatus('rerollDieFinal', notActive)
#functionEnd

#--------------------------------#
def actionPutDieBack(allText,specialVars):
#--------------------------------#
    specialVars.isDieTaken = False

    deskTag = findTag(allText,'desk')
    #activate options
    active = True
    allText[deskTag].setOptionStatus(   'takeDie'    , active)
    allText[deskTag].setOptionStatus('rerollDieFinal', active)
    #deactivate options
    notActive = False
    allText[deskTag].setOptionStatus('putDieBack', notActive)

#functionEnd

#--------------------------------#
def actionExamineDesk(allText,specialVars):
#--------------------------------#
    deskTag = findTag(allText, 'desk')
    dieStuffTxtTag = allText[deskTag].findText('DIESTUFF')
    if not specialVars.isDieTaken:
        dieText = (' Also there is a twenty-sided die resting comfortably '
        'with the "20" side on top.')
        allText[deskTag].text[dieStuffTxtTag] = dieText
    else:
        allText[deskTag].text[dieStuffTxtTag] = ''
#functionEnd

#--------------------------------#
def actionAskAboutTypicalQual (allText,specialVars):
#--------------------------------#
    #heard no new keywords

    myTag = findTag(allText,'typicalQualifications')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutEducation(allText,specialVars):
#--------------------------------#
    #heard about CFD, diplomaThesis, phdThesis
    specialVars.cfd      = True
    specialVars.diplThes = True
    specialVars.phdThes  = True
    
    myTag = findTag(allText,'eduBackground')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutTechSkills(allText,specialVars):
#--------------------------------#
    #heard about CUDAC, cfd, phd
    specialVars.CUDAC    = True
    specialVars.cfd      = True
    specialVars.phdThes  = True
    
    myTag = findTag(allText,'techSkills')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutCFD(allText,specialVars):
#--------------------------------#
    #heard no new keywords
    
    myTag = findTag(allText,'cfdExplained')
    active = True
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutCUDAC(allText,specialVars):
#--------------------------------#
    #heard no new keywords
    
    myTag = findTag(allText,'CUDAC')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutDiplThes(allText,specialVars):
#--------------------------------#
    #heard no new keywords
    
    myTag = findTag(allText,'diplomaThesisExplained')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutPhdThesisNotTech(allText,specialVars):
#--------------------------------#
    #heard about adjoint
    specialVars.adjoint = True
    
    myTag = findTag(allText,'phdThesisExplainedNotTech')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutPhdThesisLittleTech(allText,specialVars):
#--------------------------------#
    #heard about adjoint
    specialVars.adjoint = True
    
    myTag = findTag(allText,'phdThesisExplainedLittleTech')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutPhdThesisFullTech(allText,specialVars):
#--------------------------------#
    #heard about adjoint
    specialVars.adjoint = True
    
    myTag = findTag(allText,'phdThesisExplainedFullTech')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.adjoint:
        allText[myTag].setOptionStatus('adjExplained', active)
#functionEnd

#--------------------------------#
def actionAskAboutAdjoint(allText,specialVars):
#--------------------------------#
    #heard no new keywords

    myTag = findTag(allText,'adjExplained')
    active = True
    if specialVars.cfd:
        allText[myTag].setOptionStatus('cfdExplained', active)
    if specialVars.CUDAC:
        allText[myTag].setOptionStatus('CUDAC', active)
    if specialVars.diplThes:
        allText[myTag].setOptionStatus('diplomaThesisExplained', active)
    if specialVars.phdThes:
        allText[myTag].setOptionStatus('phdThesisExplained', active)
#functionEnd

#--------------------------------#
def actionGlitchInTheMatrix(allText,specialVars):
#--------------------------------#

    dialogueTag = findTag(allText,'desk')

    active = True
    allText[dialogueTag].setOptionStatus('awakenDesktop', active)

    notActive = False
    allText[dialogueTag].setOptionStatus('awakenDesktopGlitch', notActive)
#functionEnd

#--------------------------------#
def actionAwakenDesktop(allText,specialVars):
#--------------------------------#

    dialogueTag = findTag(allText,'desk')

    active = True
    allText[dialogueTag].setOptionStatus('crackDesktop', active)

    notActive = False
    allText[dialogueTag].setOptionStatus('awakenDesktop', notActive)
#functionEnd

#--------------------------------#
def actionAwakenLaptop(allText,specialVars):
#--------------------------------#

    dialogueTag = findTag(allText,'desk')

    active = True
    allText[dialogueTag].setOptionStatus('crackLaptop', active)

    notActive = False
    allText[dialogueTag].setOptionStatus('awakenLaptop', notActive)
#functionEnd

#--------------------------------#
def actionCoffee(allText,specialVars):
#--------------------------------#
    specialVars.coffee = True
#functionEnd

#--------------------------------#
def actionTea(allText,specialVars):
#--------------------------------#
    specialVars.tea = True
#functionEnd

#--------------------------------#
def actionHotChoco(allText,specialVars):
#--------------------------------#
    specialVars.hotChoco = True
#functionEnd

#--------------------------------#
def actionNoDrink(allText,specialVars):
#--------------------------------#
    specialVars.nothing = True
#functionEnd

#--------------------------------#
def actionBeverages(allText,specialVars):
#--------------------------------#
    w8ForHimTag = findTag(allText, 'w8ForHim')
    beveragesTxtTag = allText[w8ForHimTag].findText('BEVERAGES')
    if specialVars.coffee:
        allText[w8ForHimTag].text[beveragesTxtTag] = 'two cups of coffee'
    elif specialVars.tea:
        allText[w8ForHimTag].text[beveragesTxtTag] = 'a cup of coffee and a cup of tea'
    elif specialVars.hotChoco:
        allText[w8ForHimTag].text[beveragesTxtTag] = 'a cup of coffee and a cup of hot chocolate'
    elif specialVars.nothing:
        allText[w8ForHimTag].text[beveragesTxtTag] = 'a cup of coffee and a glass of water'
#functionEnd

#--------------------------------#
def actionGoodEnding(allText,specialVars):
#--------------------------------#
    if specialVars.isDieTaken:
        goodInterviewTag = findTag(allText, 'goodInterview')
        dieStuffTxtTag = allText[goodInterviewTag].findText('DIESTUFF')
        allText[goodInterviewTag].text[dieStuffTxtTag] = ' And the best of all? Today you found a magical die!'
#functionEnd

#--------------------------------#
def actionBadEnding(allText,specialVars):
#--------------------------------#
    specialVars.goodEnding = False
    if specialVars.isDieTaken:
        badInterviewTag = findTag(allText, 'badInterview')
        dieStuffTxtTag = allText[badInterviewTag].findText('DIESTUFF')
        allText[badInterviewTag].text[dieStuffTxtTag] = ' Even worse! You also took his magical die!'
#functionEnd
