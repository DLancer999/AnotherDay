#  
# Copyright (c) Kavvadias Ioannis. All rights reserved.  
# email: kavvadiasj@hotmail.com
#

from functions import *
from actionFunctions import *

#--------------------------------#
def initializeScript():
#--------------------------------#
    #list containing all script
    allText = []

    NA = 'unreachable' #should not be seen during gamePlay
    cnt = 'continue'

    #create dialogue text
    buildingEntrance = dialogue(allText, 'buildingEntrance', NA, 'yes')

    buildingEtranceText = ('What a weird day. As if you hadn\'t had enough work to do, let '
        'alone being a rush hour, they sent you to interview a guy at his house. Who is this '
        'Kavvadias Giannis anyway? Feeling irritated, you enter his apartment block. '
        'Based on the position of his doorbell '
        'his apartment should be on the  fifth floor.')
    buildingEntrance.addText(buildingEtranceText)

    takeStairs = dialogue(allText, 'stairs', 'Take the stairs', NA)
    takeStairsText = ( 'As you take the stairs you keep reminding yourself how important '
        'it is to work out. Especially near the top where you have run out of breath. '
        'Nevertheless you feel proud of yourself.')
    takeStairs.addText(takeStairsText)

    takeElevator = dialogue(allText, 'elevator', 'Take the elevator', NA)
    takeElevatorText = ( 'Luckily the elevator is already on the ground floor. There is '
        'a pleasant music playing in the elevator which somehow soothes you from this already '
        'stressful day.')
    takeElevator.addText(takeElevatorText)

    apartmentDoor = dialogue(allText, 'apartmentDoor', cnt, NA,actionApartmentDoor)
    apartmentDoorText=( 'As you reach the fifth floor, you see a tall Caucasian male with short '
        'dark hair waiting for you at the door. "Hello, ')
    apartmentDoor.addText(apartmentDoorText)
    apartmentDoor.addText('','INTERVIEWERSNAME',True)
    apartmentDoor.addText(' I presume", he says.','',True)

    greeting1 = dialogue(allText, 'politeGreeting1', '"Yes, I am here for the interview."',                 NA)
    greeting2 = dialogue(allText, 'politeGreeting2', '"Hello Mr. Kavvadias, I am here for the interview."', NA)
    greeting3 = dialogue(allText, 'politeGreeting3', '"Hello Dr. Kavvadias, I am here for the interview."', NA)

    answer = '"Nice to meet you'
    answer2= ', I\'m Kavvadias Giannis' 
    answer3=('", he says as he gives you a firm handshake. He steps back from ' 
             'the door and welcomes you to his house. ')
    greeting1.addText(answer+answer2+answer3)
    greeting2.addText(answer+        answer3)
    greeting3.addText(answer+        answer3)

    houseEntrance = dialogue(allText, 'houseEntrance', cnt, NA)
    houseEntranceText= ('Upon entering, you see a spacious room which seems to function ' 
        'as both an office and a living room. There are three other doors, two of which '
        'are closed and behind the third is fridge. It is easy to assume that this '
        'is the kitchen.')
    houseEntrance.addText(houseEntranceText)

    gettingCoffee = dialogue(allText, 'gettingCoffee', cnt, NA)
    gettingCoffee.addText('"I was just making coffee, would you like some?"')

    blackCoffee = dialogue(allText, 'blackCoffee', '"Yes please, black."', NA, actionCoffee)
    sosoCoffee  = dialogue(allText, 'sosoCoffee' , '"Yes please, with just a little sugar."',    NA, actionCoffee)
    sweetCoffee = dialogue(allText, 'sweetCoffee', '"Yes please, with a good amount of sugar."', NA, actionCoffee)

    coffeeAnswer = ('Excuse me. Please make yourself comfortable. '
        'I will be right back", he says and goes into the kitchen.')

    blackCoffee.addText('"A splendid choice, I like my coffee black as well. '+coffeeAnswer)
    sosoCoffee.addText( '"Of course. '+coffeeAnswer)
    sweetCoffee.addText('"Of course. '+coffeeAnswer)

    noCoffee    = dialogue(allText, 'noCoffee'   , '"No thank you, I am not a coffee drinker."', NA)
    noCoffee.addText('"What about some tea or some other hot beverage?"')

    drinkTea = dialogue(allText, 'drinkTea', '"Some tea would be good, thank you."',        NA, actionTea)
    hotChoco = dialogue(allText, 'hotChoco', '"A hot chocolate would be nice, thank you."', NA, actionHotChoco)
    noDrink  = dialogue(allText, 'noDrink' , '"No thank you, I am good."',                  NA, actionNoDrink)

    drinkTea.addText('"Ok! '+coffeeAnswer)
    hotChoco.addText('"Ok! '+coffeeAnswer)
    noDrink.addText( '"Ok! '+coffeeAnswer)

    examineOther= 'Nothing of further interest. Examine something else.'
    livingRoomExplore = dialogue(allText, 'livingRoomExplore', cnt, examineOther)
    livingRoomExploreText = ( 'You are standing in the middle of the living room. ' 
        'Giannis is in the kitchen making coffee. On the left side of the room, '
        'right next to his desk, is a big library. Next to it are a bunch of '
        'certificates and diplomas hanging on the wall. In front of you is a sofa '
        'opposing a big TV monitor. ') 
    livingRoomExplore.addText(livingRoomExploreText)

    library  = dialogue(allText, 'library', 'Examine his library', examineOther)
    library.addText('The library has four selves, with each containing different kind of items.')

    shelf1 = dialogue(allText, 'shelf1', 'Examine first self (contains his theses and other papers)', examineOther) 
    shelf1Text = ( 'In this self you see his PhD thesis, his diploma thesis and a bunch '
        'of scientific papers.')
    shelf1.addText(shelf1Text)

    phdThesis = dialogue(allText, 'phdThesis', 'Examine his PhD thesis', examineOther)
    phdThesisText = ( '"Continuous Adjoint Methods for Steady and Unsteady Turbulent flows '
        'with Emphasis on the Accuracy of Sensitivity Derivatives". It looks impressive, '
        'but he would probably return before you had enough time to read it.')
    phdThesis.addText(phdThesisText)
     
    diplomaThesis = dialogue(allText, 'diplomaThesis', 'Examine his diploma thesis', examineOther)
    diplomaThesisText = ( '"Programming of a GPU-enabled 3D Euler equations\' solver '
        'on structured grids". It looks like he knows his way around a GPU. Good to know.')
    diplomaThesis.addText(diplomaThesisText)

    papers = dialogue(allText, 'papers', 'Examine the scientific papers', examineOther)
    papersText = ( 'There are many scientific papers on optimization and design methods, '
        'computational fluid dynamics and numerical methods. He is '
        'coauthor in some of them.')
    papers.addText(papersText)

    shelf2 = dialogue(allText, 'shelf2', 'Examine second self (contains scientific books and manuals)', examineOther) 
    shelf2Text = ( 'In this shelf he keeps scientific books for fluid mechanics, physics and '
        'linear algebra. Also, there are many books about programming, mostly for C++ '
        '(it looks like everyone has a Stroustrup book in their library) and program '
        'manuals for various software. Among others you notice some manuals for ' 
        '3D modeling software and different game Engines.')
    shelf2.addText(shelf2Text)

    shelf3 = dialogue(allText, 'shelf3', 'Examine third self (contains literature books)', examineOther) 
    shelf3Text = ( 'In this self there are some high fantasy novels and a lot of RPG rule books. '
        'That is a lot of RPG rule books!')
    shelf3.addText(shelf3Text)

    shelf4 = dialogue(allText, 'shelf4', 'Examine forth self (contains movies and computer/console games)', examineOther) 
    shelf4Text = ( 'Here he keeps his movies, most of which are either filmed on high budget '
        'with awesome visual effects or they are medieval in setting. Also he has his video '
        'games stacked next to the movies. Most of them are for PC with some for '
        'consoles. There are a lot of beat\'em up, RPGs and action games. Probably '
        'he doesn\'t like adventure games.')
    shelf4.addText(shelf4Text)

    wall     = dialogue(allText, 'wall'   , 'Examine his certificates on the wall', examineOther)
    wallText = ( 'On the top, there are his bachelor and doctoral degrees, from the Mechanical '
        'Engineering section of the National Technical University of Athens (NTUA). '
        'Below these two, there is a C2 certificate from the Hellenic American union. '
        'Also, there are many certificates full of ideograms. One of them is a '
        'beginners certificate in the Japanese while the rest of them are rank '
        'certificates in different martial arts. This could be handy in case '
        'corporate spies ever infiltrate our grounds!')
    wall.addText(wallText)

    tvSet    = dialogue(allText, 'tvSet'  , 'Examine his TV set', examineOther)
    tvSetText = ( 'As you take a closer look to the TV monitor, a 40-42" one, you '
        'notice a sub-woofer beneath it, matched with a full 7-1 surround system '
        'set-up all around the living room. Next to the sub-woofer there are '
        'a few game consoles. Actually... the sofa is too close '
        'to the screen! Probably it was put there for optimal gaming experience!')
    tvSet.addText(tvSetText)

    desk     = dialogue(allText, 'desk'   , 'Examine his desk', examineOther, actionExamineDesk)
    deskText = ( 'The first thing that pops into your mind as you look at his desk is that '
        'it is neatly organized, too neatly organized. No engineer that you know keeps his ' 
        'desk that organized. He surely did that because he was expecting you. Nevertheless, '
        'he gets points for effort. On it, there are a desktop with two monitors plugged in '
        'and a laptop, both of which are on standby mode. ')
    desk.addText(deskText)
    desk.addText('','DIESTUFF',True)

    awakenDesktopGlitch= dialogue(allText, 'awakenDesktopGlitch', 'Examine his desktop', NA)
    awakenDesktopGlitchText = ('While you normally know better than to mess around other people\'s '
        'computers without their permission, you nudge the mouse to awaken '
        'the desktop. A console terminal is open prompting you to give a character name.') 
    awakenDesktopGlitch.addText(awakenDesktopGlitchText)

    glitchText = ('A text message appears on screen saying "'+ buildingEtranceText + '"')

    glitch1 = dialogue(allText, 'glitch1', 'Insert your name', NA)
    glitch1.addText(glitchText)

    glitch2 = dialogue(allText, 'glitch2', 'Insert random name', NA)
    glitch2.addText(glitchText)

    finalGlitch = dialogue(allText, 'finalGlitch', '...', NA, actionGlitchInTheMatrix)
    finalGlitchText = ('Wait... why are there two identical black cats passing by the window?')
    finalGlitch.addText(finalGlitchText)

    awakenDesktop = dialogue(allText, 'awakenDesktop', 'Awaken his desktop', NA, actionAwakenDesktop)
    awakenDesktopText = ('While you normally know better than to mess around other people\'s '
        'computers without their permission, you nudge the mouse to awaken '
        'the desktop. In the Windows login screen, you are prompted for a password.') 
    awakenDesktop.addText(awakenDesktopText)

    crackDesktop = dialogue(allText, 'crackDesktop', 'Crack Desktop password', 'Try something else')
    crackDesktop.addText('To crack the password you')

    awakenLaptop  = dialogue(allText, 'awakenLaptop',  'Awaken his laptop' , NA, actionAwakenLaptop)
    awakenLaptopText = ( 'While you normally know better than to mess around other people\'s '
        'computers without their permission, you press the power button to awaken the laptop. '
        'In the Ubuntu login screen, you are prompted for a password.') 
    awakenLaptop.addText(awakenLaptopText)

    crackLaptop = dialogue(allText, 'crackLaptop', 'Crack Laptop password', 'Try something else')
    crackLaptop.addText('To crack the password you')

    passDeclined = 'A wrong-password message comes on screen.'
    randomPassword1 = dialogue(allText, 'randomPassword1', 'Insert "123456"',   NA)
    randomPassword2 = dialogue(allText, 'randomPassword2', 'Insert "password"', NA)
    randomPassword3 = dialogue(allText, 'randomPassword3', 'Insert "dragon"',   NA)
    randomPassword4 = dialogue(allText, 'randomPassword4', 'Insert "qwerty"',   NA)
    randomPassword5 = dialogue(allText, 'randomPassword5', 'Insert "monkey"',   NA)
    randomPassword6 = dialogue(allText, 'randomPassword6', 'Insert "superman"', NA)

    randomPassword1.addText(passDeclined)
    randomPassword2.addText(passDeclined)
    randomPassword3.addText(passDeclined)
    randomPassword4.addText(passDeclined)
    randomPassword5.addText(passDeclined)
    randomPassword6.addText(passDeclined)

    rebootDesktop = dialogue(allText, 'rebootDesktop', 'Reboot and boot in safe mode', NA)
    rebootDesktopText = ( 'The booting sequence takes its time. An SSD drive could help '
        'with the performance of this computer. So you wait for it to boot.')
    rebootDesktop.addText(rebootDesktopText)

    rebootLaptop  = dialogue(allText, 'rebootLaptop', 'Reboot and boot as single user', NA)
    rebootLaptopText = ( 'You do what you have to do and the prompt "Change root user password" '
        'appears on screen.')
    rebootLaptop.addText(rebootLaptopText)

    getCaught = dialogue(allText, 'getCaught', cnt, NA)
    getCaughtText = ( '"Excuse me! What are you doing there?", you hear Giannis saying '
        'coming back from the kitchen holding a tray.')
    getCaught.addText(getCaughtText)

    randomExcuse1 = dialogue(allText, 'randomExcuse1', '"Erm, I was just looking for the time..."', NA)
    randomExcuse2 = dialogue(allText, 'randomExcuse2', '"Erm, I was just checking the weather..."', NA)
    randomExcuse3 = dialogue(allText, 'randomExcuse3', '"Erm, nothing?..."', NA)

    excused = ('Without paying attention to your random excuse, he sees the monitor and '
        'understands exactly what you were trying to do! "I have to ask you to leave '
        'right now!" he says firmly.') 

    randomExcuse1.addText(excused)
    randomExcuse2.addText(excused)
    randomExcuse3.addText(excused)

    justLeave = dialogue(allText, 'justLeave', 'Accept your mistake and leave the premises', NA, actionBadEnding)
    justLeaveText = ( 'As you leave, you just cannot stop feeling mad at yourself for the way '
        'you behaved. Even worse yet, what are you going to tell your boss? Surely you cannot '
        'tell him that you tried to crack the candidate\'s computer! Not a good day... for sure!')
    justLeave.addText(justLeaveText)

    chargeHim = dialogue(allText, 'chargeHim', 'Panic and charge him!', NA)
    chargeHimText = ( 'Without thinking it through, you unleash your best war cry and charge him! '
        'Your jaw is now good friends with the tray he was holding!')
    chargeHim.addText(chargeHimText)

    knockedOut = dialogue(allText, 'knockedOut', cnt, NA, actionBadEnding)
    knockedOutText = ( 'You wake up sometime later, feeling quite dizzy. The first thing you see '
        'is your boss talking to a cop. This probably won\'t end well! Not a good day... for sure!')
    knockedOut.addText(knockedOutText)
    knockedOut.lastParagraph = True

    rollDie       = dialogue(allText, 'rollDie',  'Roll the die' , NA)
    rollDie.addText('"20"! This looks like a good die!')

    rerollStrng = 'Reroll the die'
    rerollDie1    = dialogue(allText, 'rerollDie1',  rerollStrng , NA)
    rerollDie1.addText('"20"! Again? This doesn\'t look normal!')

    rerollDie2    = dialogue(allText, 'rerollDie2',  rerollStrng , NA)
    rerollDie2.addText('"20"! What kind of sorcery is this?')

    rerollDie3    = dialogue(allText, 'rerollDie3',  rerollStrng , NA, actionIdentifyDie)
    rerollDie3.addText('"20"! This die is enchanted for sure!')

    rerollDieFinal    = dialogue(allText, 'rerollDieFinal',  rerollStrng , rerollStrng)
    rerollDieFinal.addText('"20"! Yep... still the same perfect roll!')

    takeDie       = dialogue(allText, 'takeDie', 'Take die', NA, actionTakeDie)
    takeDieText = ( 'You check that Giannis is still in the kitchen and quickly put '
        'the die in your pocket. ***Chaotic +5***')
    takeDie.addText(takeDieText)

    putDieBack = dialogue(allText, 'putDieBack', 'Put die back', NA, actionPutDieBack)
    putDieBackText = ( 'Feeling guilty that you took this unique magical artifact, '
        'you put it back in its original position.')
    putDieBack.addText(putDieBackText)

    w8ForHim = dialogue(allText, 'w8ForHim', 'sit on the sofa and wait for him to come back', NA, actionBeverages)
    w8ForHimText = ( 'After a couple of minutes, Giannis comes out of the kitchen, holding a '
        'tray with ') 
    w8ForHim.addText(w8ForHimText)
    w8ForHim.addText('','BEVERAGES',True)
    w8ForHimText = ( '. He on the sofa waiting for you to start the interview.')
    w8ForHim.addText(w8ForHimText,'',True)

    askOther = 'Talk about something else'
    interviewStart = dialogue(allText, 'interviewStart', 'Start interview', askOther)
    interviewStart.addText('You\'d like to')

    typicalQualifications = dialogue(allText, 'typicalQualifications', 'ask about his standard qualifications', askOther, actionAskAboutTypicalQual)
    typicalQualifications.addText('Giannis is waiting for your questions.')

    eduBackground = dialogue(allText, 'eduBackground', '"Where and what did you study?"', NA, actionAskAboutEducation)
    eduBackgroundText = ( '"I did my bachelor studies, or master... it is a five-year-long '
        'course cycle... call it whatever, as a mechanical engineer in the National Technical '
        'University of Athens, or NTUA for short. I did my diploma thesis at the fluids section, '
        'where I also continued afterwards and earned my PhD in optimization and design methods, for CFD '
        'applications. I finished my PhD last February. After that I went to fulfill '
        'the Greek mandatory military service and currently I am working as postdoctoral '
        'researcher at NTUA."')
    eduBackground.addText(eduBackgroundText)

    techSkills = dialogue(allText, 'techSkills', '"What are your technical skills?"', NA, actionAskAboutTechSkills)
    techSkillsText = ( '"Programming wise, I am an expert C++ programmer and can comfortably '
        'work with any C-based language, including CUDA-C. My scripting is done either '
        'in Python or Bash. Should the need arise, I find it really easy to adapt to '
        'different languages. Other than that, my linear algebra skills are in excellent '
        'condition, thanks to my CFD background, and I have broad knowledge of fluid mechanics '
        'and optimization methods, which was the topic of my PhD."')
    techSkills.addText(techSkillsText)

    cfdExplained = dialogue(allText, 'cfdExplained', '"What is this CFD you mentioned?"', NA, actionAskAboutCFD)
    cfdExplainedText = ( '"CFD is short for computational fluid dynamics. It\'s a branch of '
        'fluid mechanics, where the flow is predicted through numerical analysis and '
        'computer simulation."')
    cfdExplained.addText(cfdExplainedText)

    CUDAC = dialogue(allText, 'CUDAC', '"Why did you point CUDA-C out of the rest of the C-based languages?"', NA, actionAskAboutCUDAC)
    CUDACText = ( '"Well, while it is relatively easy to learn the five, ten, fifty new commands '
        'required to work on a different language, the difficult/interesting thing is '
        'to start thinking in the optimal way to make the most out of your tools. '
        'For CUDA, this is to embrace the parallel nature of the GPU and play along. '
        'This requires a \'rewriting\' of your thinking. You have to start thinking in '
        'parallel to make the most out of it. This is not the case, for instance, with C#."')
    CUDAC.addText(CUDACText)

    diplomaThesisExplained = dialogue(allText, 'diplomaThesisExplained', '"What was your diploma thesis about?"', NA, actionAskAboutDiplThes)
    diplomaThesisExplainedText = ('"Well, in one sentence, it was about the optimal utilization '
        'of the gpu for CFD applications. What I actually did, if you are interested in that, is '
        'the programming of an Euler solver, a solver for the inviscid fluid equations for '
        'structured grids. Then I compared the performance of the GPU-enabled solver to that '
        'of the in-house CPU solver, with the first being a bit less than two orders of '
        'magnitude faster."')
    diplomaThesisExplained.addText(diplomaThesisExplainedText)

    phdThesisExplained = dialogue(allText, 'phdThesisExplained', '"What was the topic of your PhD?"', NA)
    phdThesisExplainedText = ('"To tune the technical talk to the correct amount, allow me to '
        'ask you first... what is your background?"')
    phdThesisExplained.addText(phdThesisExplainedText)

    phdThesisExplainedNotTech = dialogue(allText, 'phdThesisExplainedNotTech', '"I have nothing to do with math and physics!"', '"... Which is translated in English as?"', actionAskAboutPhdThesisNotTech)
    phdThesisExplainedNotTechText = ('"The simplest way to describe it would be to say '
        'that I designed cars. As you can guess it is an oversimplification, and somewhat wrong. '
        'What I actually did was to formulate and program a novel design '
        'approach, based on the so-called adjoint methods, which was mainly used for industrial '
        'vehicle design. This method highlights what is wrong with a given aerodynamical design, '
        'which could be a car, and proposes a way to optimize it, to make it '
        'better with respect to some design target. A usual target for car applications '
        'is to minimize the drag force of the vehicle, in which case it could propose to install '
        'a spoiler in the back of it or propose a way to optimize an already existing one."')
    phdThesisExplainedNotTech.addText(phdThesisExplainedNotTechText)

    phdThesisExplainedLittleTech = dialogue(allText, 'phdThesisExplainedLittleTech', '"I have an approximate knowledge of math and physics!"', '"Can you tone down the technical details a bit?"', actionAskAboutPhdThesisLittleTech)
    phdThesisExplainedLittleTechText = ('"Well, my PhD was in the field of deterministic optimization '
        'methods, for aerodynamic applications, using the continuous adjoint method. '
        'Applications '
        'of it includes anything that can be modeled through the turbulent Navier-Stokes '
        'Equations, the equations for fluid motion in turbulent conditions. Some examples are '
        'flows in ducts, like ventilation, flows around wings and airfoils or more complex '
        'industrial applications like turbomachines, cars, trains, airplanes, wind turbines '
        'and so on. To use any deterministic optimization method, the sensitivity derivative '
        'of an objective function is required, i.e. how the \'efficiency\' of a design is '
        'changed with respect to change in some predefined design control variable. '
        'For instance, if someone tries to find the best car height for minimum drag, '
        'i.e. the least amount of resistance due to air friction, the sensitivity derivative '
        'is how the drag force changes with respect to some change in the car height. The '
        'fast and accurate computation of said sensitivity derivatives, which can be much '
        'much more than a single one, is of utmost importance in deterministic optimization methods. '
        'My work expanded this continuous adjoint method to be able to compute fast and '
        'accurate sensitivity derivatives in complex turbulent cases, such as those '
        'encountered in real-world industrial applications, like the flow around a sports car '
        'or inside a turbomachine."')
    phdThesisExplainedLittleTech.addText(phdThesisExplainedLittleTechText)

    phdThesisExplainedFullTech = dialogue(allText, 'phdThesisExplainedFullTech', '"Feel free to talk about it any way you like!"', NA, actionAskAboutPhdThesisFullTech)
    phdThesisExplainedFullTechText = ('After a somewhat evil grin he starts talking. '  
        '"For my PhD, I worked on the mathematical formulation, programming '
        'and validation of continuous adjoint methods to steady and unsteady turbulent '
        'flows with emphasis on the accuracy of the computed sensitivity derivatives for '
        'objective functions related to aerodynamics. Applications included shape and '
        'flow-control optimization problems in internal and external flows of both '
        'academic and industrial origin. Important contributions included, among others, '
        'the analytic differentiation of the k-ω SST turbulence model and a novel adjoint '
        'formulation which can compute sensitivity derivatives with the accuracy of the '
        'most accurate continuous adjoint formulation and as fast as the fastest one."')
    phdThesisExplainedFullTech.addText(phdThesisExplainedFullTechText)

    adjExplained = dialogue(allText, 'adjExplained', '"What is this adjoint you mentioned?"', NA, actionAskAboutAdjoint)
    adjExplainedText = ('"Adjoint, not to be confused with the classical adjoint of linear '
        'algebra, is a mathematical trick to efficiently compute the sensitivity '
        'derivative, the gradient of a function, with respect to a design variable, the '
        'control variable of the problem. It is usually called the dual problem because '
        'the adjoint problem shares some attributes of the original, but not exactly. '
        'It is better to think of it like witchcraft... where witches are mathematicians, '
        'adjoint is a big spoon and the optimization problem is the cauldron! Wait, '
        'I don\'t think that this makes any sense... but then again math sure sounds weird '
        'some times!"')
    adjExplained.addText(adjExplainedText)

    obscureQuestions = dialogue(allText, 'obscureQuestions', 'go for more obscure questions', askOther)
    obscureQuestions.addText('Giannis is waiting for your questions.')

    disadvantages = dialogue(allText,'disadvantages', '"What are your biggest advantages and disadvantages?"', NA)
    disadvantagesText = ( '"Well, I see myself as a perfectionist. Most of the times that is a '
        'good thing. A very good thing that, backed-up by the right conditions, can lead to '
        'beautiful outcomes. On the other hand, sometimes I\'ve caught myself obsessing about '
        'stuff that are not that important. I am working on keeping only the good aspect of '
        'it, but you know, progress takes time!"')
    disadvantages.addText(disadvantagesText)

    motivation = dialogue(allText,'motivation', '"What motivates you?"', NA)
    motivationText = ( '"To never stop evolving! Whenever I look back I want to see things '
        'that the new-me is better than the old-me!"')
    motivation.addText(motivationText)

    workEnviroment = dialogue(allText,'workEnviroment', '"What are you looking for in your work?"', NA)
    workEnviromentText = ( '"In my work, I look for the opportunity to create something '
        'to be proud of! In my working environment, I am looking for same minded people '
        'who would like to do the same!"')
    workEnviroment.addText(workEnviromentText)

    yourself = dialogue(allText, 'yourself', '"Tell me a few things about yourself."', NA)
    yourselfText = ( '"Err, that\'s a tough one. Let\'s see... I\'m a passionate gamer, '
        'playing both board and electronic games, I like all things medieval and nothing '
        'beats a good fantasy movie! When I am not in front of a monitor, I like to train. '
        'You see, I\'ve been a martial artist for almost all my life. Travelling is '
        'always fun as well, but unfortunately, I seldom find time for it!"')
    yourself.addText(yourselfText)

    aggressiveQuestions = dialogue(allText, 'aggressiveQuestions', 'sweat him a little', askOther)
    aggressiveQuestions.addText('Giannis is waiting for your questions.')

    corpGain = dialogue(allText, 'corpGain', '"What do you have to offer to our team?"', NA)
    corpGainText =('"My years as a PhD candidate have equipped me with an arsenal indispensable in ' 
        'your field of work. First of all, when doing research, you stop looking at ' 
        'things as they are and start visualize them as they could be. After a while, '
        'it comes naturally to evaluate which areas of a project are good as-is, which require ' 
        'tweaks and optimizing and which need reworking from the bottom-up. Of course, this comes ' 
        'together with acute critical thinking and problem solving capabilities. ' 
        'Equally important are my team working abilities. I can communicate complex ' 
        'concepts in simple terms, cooperate with people of different specialties ' 
        'without problems and constructive criticism is always welcomed."') 
    corpGain.addText(corpGainText)

    corpHire = dialogue(allText, 'corpHire', '"Why should we hire you?"', NA)
    corpHireText = ( '"Well, let\'s see... Based on my technical skills, I would be a ' 
        'great addition to your group right from the start. With programming being my greatest ' 
        'passion, and the relevant mathematical and physics knowledge to back-it up, '
        'I will be able to rise to the occasion to any challenge encountered in this ' 
        'field of work. Also I am very driven on constantly honing my skills on every level ' 
        'and looking for opportunities to expand my abilities in new ways! ' 
        'Also, equally important are my team playing abilities which allow me to cooperate ' 
        'efficiently with people of diverse background to utilize each other\'s unique ' 
        'strengths and produce results worthy of praise!"') 
    corpHire.addText(corpHireText)

    corpSpecificQuestions = dialogue(allText, 'corpSpecificQuestions', 'discuss stuff regarding your team', askOther)
    corpSpecificQuestionsText = ( 'You just remembered that the higher-ups told you not to discuss '
        'anything regarding your company. Instead, if the interview is going well, you should '
        'invite him in for a follow-up interview at the company.')
    corpSpecificQuestions.addText(corpSpecificQuestionsText)

    interviewEnd = dialogue(allText, 'interviewEnd', 'end interview', NA)
    interviewEndText = ( 'Are you sure that you have learned enough about this participant '
        'to end the interview?')
    interviewEnd.addText(interviewEndText)

    contInterview = dialogue(allText, 'contInterview', 'No', NA)
    contInterview.addText('Then you should continue asking questions.')

    closingRemark = dialogue(allText, 'closingRemark', 'Yes', NA) 
    closingRemark.addText('Giannis is waiting for you to comment on the outcome of the interview!')

    goodbyeText = ( '"Thank you Giannis for your time, it was a pleasure to meet you and I '
        'believe you will fit right into our team. You will hear from us soon '
        'to arrange a secondary meeting in our location!"')
    goodInterview = dialogue(allText,'goodInterview', goodbyeText, NA, actionGoodEnding)
    goodInterviewText = ( 'You discuss for some time more and then you get up to '
        'go back to your daily routine. After all, this was not a waste of your time. '
        'You met a promising candidate with lots of potential. Your higher ups will be pleased '
        'to hear that. It is a good day after all!')
    goodInterview.addText(goodInterviewText)
    goodInterview.addText('','DIESTUFF',True)
    goodInterview.lastParagraph = True

    badbyeText  = ('"Thank you Giannis for your time, unfortunately you are not what we '
        'are looking for at the moment. Good luck in your future endeavors!"')
    badInterview = dialogue(allText,'badInterview' , badbyeText , NA, actionBadEnding)
    badInterviewText = ( 'As soon as the interview is over you get up to go back '
        'to your daily routine. Unfortunately there is no free position he could '
        'fill at the moment. What\'s worse is that you actually liked that guy. '
        'You should keep him in mind in case a new position opens up. For the '
        'time being though, he still has to look for a job.')
    badInterview.addText(badInterviewText)
    badInterview.addText('','DIESTUFF',True)
    badInterview.lastParagraph = True

    #set dialogue interactions

    goToOpt   = True 
    rtrnOpt   = False 
    notActive = False #can be activated through interactions

    buildingEntrance.addOption(takeStairs  )
    buildingEntrance.addOption(takeElevator)

    takeStairs.addOption(apartmentDoor)

    takeElevator.addOption(apartmentDoor)

    apartmentDoor.addOption(greeting1)
    apartmentDoor.addOption(greeting2)
    apartmentDoor.addOption(greeting3)

    greeting1.addOption(houseEntrance)
    greeting2.addOption(houseEntrance)
    greeting3.addOption(houseEntrance)

    houseEntrance.addOption(gettingCoffee)

    gettingCoffee.addOption(blackCoffee)
    gettingCoffee.addOption(sosoCoffee )
    gettingCoffee.addOption(sweetCoffee)
    gettingCoffee.addOption(noCoffee   )

    blackCoffee.addOption(livingRoomExplore)
    sosoCoffee.addOption(livingRoomExplore) 
    sweetCoffee.addOption(livingRoomExplore)

    noCoffee.addOption(drinkTea) 
    noCoffee.addOption(hotChoco) 
    noCoffee.addOption(noDrink) 

    drinkTea.addOption(livingRoomExplore)
    hotChoco.addOption(livingRoomExplore)
    noDrink.addOption(livingRoomExplore)

    livingRoomExplore.addOption(library )
    livingRoomExplore.addOption(wall    )
    livingRoomExplore.addOption(tvSet   )
    livingRoomExplore.addOption(desk    )
    livingRoomExplore.addOption(w8ForHim)

    library.addOption(shelf1)
    library.addOption(shelf2)
    library.addOption(shelf3)
    library.addOption(shelf4)
    library.addOption(livingRoomExplore,rtrnOpt)

    shelf1.addOption(phdThesis)
    shelf1.addOption(diplomaThesis)
    shelf1.addOption(papers)
    shelf1.addOption(library, rtrnOpt)

    phdThesis.addOption(shelf1,rtrnOpt)
    diplomaThesis.addOption(shelf1,rtrnOpt)
    papers.addOption(shelf1,rtrnOpt)

    shelf2.addOption(library,rtrnOpt)
    shelf3.addOption(library,rtrnOpt)
    shelf4.addOption(library,rtrnOpt)

    wall.addOption(livingRoomExplore,rtrnOpt)
    tvSet.addOption(livingRoomExplore,rtrnOpt)

    desk.addOption(awakenDesktopGlitch)
    desk.addOption(awakenDesktop,goToOpt,notActive)
    desk.addOption(crackDesktop,goToOpt,notActive)
    desk.addOption(awakenLaptop)
    desk.addOption(crackLaptop,goToOpt,notActive)
    desk.addOption(rollDie)
    desk.addOption(rerollDieFinal,goToOpt,notActive)
    desk.addOption(takeDie,goToOpt,notActive)
    desk.addOption(putDieBack,goToOpt,notActive)
    desk.addOption(livingRoomExplore,rtrnOpt)

    awakenDesktopGlitch.addOption(glitch1)
    awakenDesktopGlitch.addOption(glitch2)
    awakenDesktopGlitch.addOption(desk,rtrnOpt)

    glitch1.addOption(finalGlitch)

    glitch2.addOption(finalGlitch)

    finalGlitch.addOption(desk,rtrnOpt)

    awakenDesktop.addOption(crackDesktop)
    awakenDesktop.addOption(desk,rtrnOpt)

    crackDesktop.addOption(randomPassword1)
    crackDesktop.addOption(randomPassword2)
    crackDesktop.addOption(randomPassword3)
    crackDesktop.addOption(rebootDesktop)
    crackDesktop.addOption(desk,rtrnOpt)

    randomPassword1.addOption(crackDesktop,rtrnOpt)
    randomPassword2.addOption(crackDesktop,rtrnOpt)
    randomPassword3.addOption(crackDesktop,rtrnOpt)

    awakenLaptop.addOption(crackLaptop)
    awakenLaptop.addOption(desk,rtrnOpt)

    crackLaptop.addOption(randomPassword4)
    crackLaptop.addOption(randomPassword5)
    crackLaptop.addOption(randomPassword6)
    crackLaptop.addOption(rebootLaptop)
    crackLaptop.addOption(desk,rtrnOpt)

    randomPassword4.addOption(crackLaptop,rtrnOpt)
    randomPassword5.addOption(crackLaptop,rtrnOpt)
    randomPassword6.addOption(crackLaptop,rtrnOpt)

    rebootDesktop.addOption(getCaught)
    rebootLaptop.addOption(getCaught)

    getCaught.addOption(randomExcuse1)
    getCaught.addOption(randomExcuse2)
    getCaught.addOption(randomExcuse3)
    getCaught.addOption(chargeHim)

    randomExcuse1.addOption(justLeave)
    randomExcuse1.addOption(chargeHim)

    randomExcuse2.addOption(justLeave)
    randomExcuse2.addOption(chargeHim)

    randomExcuse3.addOption(justLeave)
    randomExcuse3.addOption(chargeHim)

    chargeHim.addOption(knockedOut)

   #knockedOut.addOption(badEnding)

   #justLeave.addOption(badEnding)

    rollDie.addOption(rerollDie1)
    rollDie.addOption(desk,rtrnOpt)

    rerollDie1.addOption(rerollDie2)
    rerollDie1.addOption(desk,rtrnOpt)

    rerollDie2.addOption(rerollDie3)
    rerollDie2.addOption(desk,rtrnOpt)

    rerollDie3.addOption(rerollDieFinal)
    rerollDie3.addOption(takeDie)
    rerollDie3.addOption(desk,rtrnOpt)

    rerollDieFinal.addOption(rerollDieFinal,rtrnOpt)
    rerollDieFinal.addOption(takeDie)
    rerollDieFinal.addOption(desk,rtrnOpt)

    takeDie.addOption(desk,rtrnOpt)
    putDieBack.addOption(desk,rtrnOpt)

    w8ForHim.addOption(interviewStart)

    interviewStart.addOption(typicalQualifications)
    interviewStart.addOption(obscureQuestions)
    interviewStart.addOption(aggressiveQuestions)
    interviewStart.addOption(corpSpecificQuestions)
    interviewStart.addOption(interviewEnd)

    typicalQualifications.addOption(eduBackground)
    typicalQualifications.addOption(techSkills)
    typicalQualifications.addOption(cfdExplained,           goToOpt, notActive)
    typicalQualifications.addOption(CUDAC,                  goToOpt, notActive)
    typicalQualifications.addOption(adjExplained,           goToOpt, notActive)
    typicalQualifications.addOption(diplomaThesisExplained, goToOpt, notActive)
    typicalQualifications.addOption(phdThesisExplained,     goToOpt, notActive)
    typicalQualifications.addOption(interviewStart,         rtrnOpt)

    eduBackground.addOption(techSkills)
    eduBackground.addOption(diplomaThesisExplained,goToOpt, notActive)
    eduBackground.addOption(phdThesisExplained,    goToOpt, notActive)
    eduBackground.addOption(cfdExplained,          goToOpt, notActive)
    eduBackground.addOption(CUDAC,                 goToOpt, notActive)
    eduBackground.addOption(adjExplained,          goToOpt, notActive)
    eduBackground.addOption(interviewStart,        rtrnOpt)

    techSkills.addOption(eduBackground)
    techSkills.addOption(diplomaThesisExplained, goToOpt, notActive)
    techSkills.addOption(phdThesisExplained,     goToOpt, notActive)
    techSkills.addOption(cfdExplained,           goToOpt, notActive)
    techSkills.addOption(CUDAC,                  goToOpt, notActive)
    techSkills.addOption(adjExplained,           goToOpt, notActive)
    techSkills.addOption(interviewStart,         rtrnOpt)

    cfdExplained.addOption(eduBackground)
    cfdExplained.addOption(techSkills)
    cfdExplained.addOption(diplomaThesisExplained, goToOpt, notActive)
    cfdExplained.addOption(phdThesisExplained,     goToOpt, notActive)
    cfdExplained.addOption(CUDAC,                  goToOpt, notActive)
    cfdExplained.addOption(adjExplained,           goToOpt, notActive)
    cfdExplained.addOption(interviewStart,         rtrnOpt)

    CUDAC.addOption(eduBackground)
    CUDAC.addOption(techSkills)
    CUDAC.addOption(diplomaThesisExplained, goToOpt, notActive)
    CUDAC.addOption(phdThesisExplained,     goToOpt, notActive)
    CUDAC.addOption(cfdExplained,           goToOpt, notActive) 
    CUDAC.addOption(adjExplained,           goToOpt, notActive)
    CUDAC.addOption(interviewStart,         rtrnOpt)             

    diplomaThesisExplained.addOption(eduBackground)
    diplomaThesisExplained.addOption(techSkills)
    diplomaThesisExplained.addOption(phdThesisExplained, goToOpt, notActive)
    diplomaThesisExplained.addOption(cfdExplained,       goToOpt, notActive)
    diplomaThesisExplained.addOption(CUDAC,              goToOpt, notActive)
    diplomaThesisExplained.addOption(adjExplained,       goToOpt, notActive)
    diplomaThesisExplained.addOption(interviewStart,     rtrnOpt)             

    phdThesisExplained.addOption(phdThesisExplainedNotTech)
    phdThesisExplained.addOption(phdThesisExplainedLittleTech)
    phdThesisExplained.addOption(phdThesisExplainedFullTech)
    phdThesisExplained.addOption(interviewStart,rtrnOpt)             

    phdThesisExplainedNotTech.addOption(eduBackground)
    phdThesisExplainedNotTech.addOption(techSkills)
    phdThesisExplainedNotTech.addOption(diplomaThesisExplained,goToOpt, notActive)
    phdThesisExplainedNotTech.addOption(cfdExplained,          goToOpt, notActive)
    phdThesisExplainedNotTech.addOption(CUDAC,                 goToOpt, notActive)
    phdThesisExplainedNotTech.addOption(adjExplained,          goToOpt, notActive)
    phdThesisExplainedNotTech.addOption(interviewStart,        rtrnOpt)             

    phdThesisExplainedLittleTech.addOption(phdThesisExplainedNotTech, rtrnOpt)
    phdThesisExplainedLittleTech.addOption(eduBackground)
    phdThesisExplainedLittleTech.addOption(techSkills)
    phdThesisExplainedLittleTech.addOption(diplomaThesisExplained, goToOpt, notActive)
    phdThesisExplainedLittleTech.addOption(cfdExplained,           goToOpt, notActive)
    phdThesisExplainedLittleTech.addOption(CUDAC,                  goToOpt, notActive)
    phdThesisExplainedLittleTech.addOption(adjExplained,           goToOpt, notActive)
    phdThesisExplainedLittleTech.addOption(interviewStart,         rtrnOpt)             

    phdThesisExplainedFullTech.addOption(phdThesisExplainedLittleTech, rtrnOpt)
    phdThesisExplainedFullTech.addOption(eduBackground)
    phdThesisExplainedFullTech.addOption(techSkills)
    phdThesisExplainedFullTech.addOption(diplomaThesisExplained,goToOpt, notActive)
    phdThesisExplainedFullTech.addOption(cfdExplained,          goToOpt, notActive)
    phdThesisExplainedFullTech.addOption(CUDAC,                 goToOpt, notActive)
    phdThesisExplainedFullTech.addOption(adjExplained,          goToOpt, notActive)
    phdThesisExplainedFullTech.addOption(interviewStart,rtrnOpt)             

    adjExplained.addOption(eduBackground)
    adjExplained.addOption(techSkills)
    adjExplained.addOption(diplomaThesisExplained, goToOpt, notActive)
    adjExplained.addOption(phdThesisExplained,     goToOpt, notActive)
    adjExplained.addOption(cfdExplained,           goToOpt, notActive)
    adjExplained.addOption(CUDAC,                  goToOpt, notActive)
    adjExplained.addOption(interviewStart,         rtrnOpt)


    obscureQuestions.addOption(disadvantages)
    obscureQuestions.addOption(motivation)
    obscureQuestions.addOption(workEnviroment)
    obscureQuestions.addOption(yourself)
    obscureQuestions.addOption(interviewStart,rtrnOpt)

    disadvantages.addOption(motivation)
    disadvantages.addOption(workEnviroment)
    disadvantages.addOption(yourself)
    disadvantages.addOption(interviewStart,rtrnOpt)

    motivation.addOption(disadvantages)
    motivation.addOption(workEnviroment)
    motivation.addOption(yourself)
    motivation.addOption(interviewStart,rtrnOpt)

    workEnviroment.addOption(disadvantages)
    workEnviroment.addOption(motivation)
    workEnviroment.addOption(yourself)
    workEnviroment.addOption(interviewStart,rtrnOpt)

    yourself.addOption(disadvantages)
    yourself.addOption(motivation)
    yourself.addOption(workEnviroment)
    yourself.addOption(interviewStart,rtrnOpt)

    aggressiveQuestions.addOption(corpGain)
    aggressiveQuestions.addOption(corpHire)
    aggressiveQuestions.addOption(interviewStart,rtrnOpt)

    corpGain.addOption(corpHire)
    corpGain.addOption(interviewStart,rtrnOpt)

    corpHire.addOption(corpGain)
    corpHire.addOption(interviewStart,rtrnOpt)

    corpSpecificQuestions.addOption(interviewStart,rtrnOpt)

    interviewEnd.addOption(closingRemark)
    interviewEnd.addOption(contInterview)

    contInterview.addOption(interviewStart,rtrnOpt)

    closingRemark.addOption(goodInterview)
    closingRemark.addOption(badInterview)

    return allText
#functionEnd

