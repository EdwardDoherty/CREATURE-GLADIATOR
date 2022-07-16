# Made by Joe Doherty   July 2022
#
#
#
# CREATURE GLADIATOR!

# ====================Creature Gladiator Wish List:===================================================================
# Creature generator:
#   Count each creature wave
# High score data, saved and shown when opening the game and when losing
# Enchanted item selection during character creator
#   Enchanted items can reduce damage taken or add more chance of blocking damage or healing
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ======================================================================================================================
# WELCOME TO CREATURE GLADIATOR
# The great and evil wizard, Akozuto, is using blood magic to create
# twisted and mangled creatures. YOU MUST STOP HIM!
#
import random
import time


print("- - = = ===:::: WELCOME TO CREATURE GLADIATOR ::::=== = = - -")


# ==========CLASSES=====================CLASSES=====================CLASSES=====================CLASSES=================
# defines the player class
class Player:
    # Variables
    name = ""
    fighterClass = ""
    health = 0
    maxHealth = 0 # This is inherited from the fighterClass, do not change this to do damage to the player
    damage = 0
    maxDamage = 0 # This is inherited from the fighterClass, do not change this to do damage to the player
    moveOne = ""
    moveTwo = ""
    moveThree = ""
    moveList = []

    isBlocking = False # Set to False to start the game.
    isDead = False # Set to False to start the game.

    # initiates a new player with all of their information
    def __init__(self, name, fighterClass):
        self.name = name
        self.fighterClass = fighterClass
        self.health = fighterClass.health
        self.maxHealth = fighterClass.health
        self.damage = fighterClass.damage
        self.maxDamage = fighterClass.damage
        self.moveOne = fighterClass.moveOne
        self.moveTwo = fighterClass.moveTwo
        self.moveThree = fighterClass.moveThree
        self.playerMoveList = [self.moveOne, self.moveTwo, self.moveThree]

    # Player character description box, keeps track of current state of stats for the user
    def __repr__(self):
        description = "{name} : {fighterClass} : Health {health}|{maxHealth} : Damage {damage}|{maxDamage}".format(name=self.name, fighterClass=self.fighterClass.name, health=self.health, maxHealth=self.maxHealth, damage=self.damage, maxDamage=self.maxDamage)
        return description

    # Returns the name of the player character as a string. Sometimes useful
    def getName(self):
        return self.name

    # Returns the class name of the player character as a string. Sometimes useful
    def getClass(self):
        return self.fighterClass

    # Method for damaging the player character
    def damagePlayer(self, damage):
        # Check if blocking. If so, do no damage.
        if self.isBlocking:
            print("{name} blocked the attack!".format(name = self.name))
        # If not blocking, do damage.
        elif not self.isBlocking:
            self.health -= damage
            playerScore.subtract(damage)
            self.checkIfDead()

    def playerHealthPotion(self):
        healthLost = self.maxHealth - self.health
        if healthLost > 0:
            print("You have been given a health potion!")
            healthPotion = random.choice(range(healthLost))
            print(healthPotion, " Health added!")
            playerOne.health += healthPotion

    #defines the different moves and executes the correct move based on moveNum
    def attackMoves(self, moveNum):
        playerOne.isBlocking = False


        def battlefieldCleanUp():
            for deadEnemy in deadCreatureList:
                for enemy in creatureList:
                    if deadEnemy == enemy:
                        creatureList.remove(enemy)

        # attack One is a simple single-enemy attack, like stab. Requires player to choose an enemy
        def attackOne(self):
            damage = self.damage
            enemyChoice = enemyChoicebox()
            enemyChoice.damageCreature(damage)
            playerScore.add(damage)
            battlefieldCleanUp()
            global playersTurn
            playersTurn = False

        # attack Two is an area-of-effect attack, like slash
        def attackTwo(self):
            damage = round(self.damage / 1.5)
            for creature in creatureList:
                creature.damageCreature(damage)
                playerScore.add(damage)
            battlefieldCleanUp()
            global playersTurn
            playersTurn = False

        # attack Three is a block, negates all damage this turn. Currently a waste of time, needs fixing
        def attackThree(self):
            # damage next turn is zero
            self.isBlocking = True
            battlefieldCleanUp()
            global playersTurn
            playersTurn = False

        # Check which move has been selected. Any weird thing that gets through will just automatically block so there are no errors
        if moveNum == 1:
            attackOne(self)
        elif moveNum == 2:
            attackTwo(self)
        else:
            attackThree(self)

    def checkIfDead(self):
        if self.health <= 0:
            self.isDead = True
           #gameOver()


# ----------------------------------------------------------------------------------------------------------------------
# Defines the creature class
class Creature:
    name = "Enemy"
    creatureClass = "Rat-Slurper"
    health = 10
    damage = 10
    isBlocking = False
    isDead = False

    # define the creature's information
    def __init__(self, name, enemyClass):
        self.name = name
        self.creatureClass = enemyClass
        self.health = enemyClass.health
        self.damage = enemyClass.damage
        self.moveOne = enemyClass.moveOne
        self.moveTwo = enemyClass.moveTwo
        self.moveThree = enemyClass.moveThree
        self.enemyMoveList = [self.moveOne, self.moveTwo, self.moveThree]


    # creature description box
    def __repr__(self):
        description = "{name} : {creatureClass} | Damage: {damage}| Health: {health}|{classHealth} ".format(name=self.name, creatureClass=self.creatureClass.name, health=self.health, damage=self.damage, classHealth = self.creatureClass.health)
        return description


    # check if health has reached 0
    def checkIfDead(self):
        if self.health <= 0:
            self.isDead = True
            deadCreatureList.append(self)

    def moveChooser(self):
        moveChoice = random.choice(range(3))
        if moveChoice == 0:
            damage = round(self.damage)
        elif moveChoice == 1:
            damage = round(self.damage / 1.5)
        else:
            damage = round(self.damage / 2)
        return moveChoice, damage



    # method for damaging the creature
    def damageCreature(self, damage):
        self.health -= damage
        damageMsg = "you did {damage} to {name}".format(damage = damage, name=self.name)
        print(damageMsg)
        self.checkIfDead()
        if self.isDead:
            deadMsg = "{name} has been slain!".format(name=self.name)
            print(deadMsg)

    # method to return the name of the creature
    def getName(self):
        return self.name

    def getClass(self):
        return self.creatureClass

    # method to attack the player
    def attack(self):
        moveChoice = self.moveChooser()
        moveDamage = moveChoice[1]
        move = self.enemyMoveList[moveChoice[0]]
        playerOne.damagePlayer(moveDamage)
        print("{creature} used {move}. Damage: {damage}".format(creature = self.name, move = move, damage = moveDamage))
        global playersTurn
        playersTurn = True


#-----------------------------------------------------------------------------------------------------------------------
# Enemy Classes, eventually to be chosen at random by the PC
class EnemyClass:
    # EnemyClass objects should be used only to give their traits to creature objects!
    #
    # These variables should be set by the class initiation and then never changed inside the EnemyClass object.
    # All changes to health, damage, etc should happen in the Creature class.
    name = "Slime"
    health = 10
    damage = 10
    moveOne = ""
    moveTwo = ""
    moveThree = ""
    classMoveList = []

    def __init__(self, name, health, damage, moveOne, moveTwo, moveThree):
        self.name = name.title()
        self.health = health
        self.damage = damage
        enemyClassList.append(self)
        self.moveOne = moveOne
        self.moveTwo = moveTwo
        self.moveThree = moveThree
        self.classMoveList = [self.moveOne, self.moveTwo, self.moveThree]

    def __repr__(self):
        description = "{name}: {health} health | {damage} damage".format(name=self.name, health=self.health, damage=self.damage)
        return description

    def getName(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------
# These are classes that a player can choose from in the beginning of the game
class PlayerClass:
    # PlayerClass objects should be used only to give their traits to the Player object.
    #
    # These variables should be set by the class initiation and then never changed inside the PlayerClass object.
    # All changes to health, damage, etc should happen in the player class.
    name = "Wimp"
    health = 10
    damage = 10
    moveOne = ""
    moveTwo = ""
    moveThree = ""
    classMoveList = []

    def __init__(self, name, health, damage, moveOne, moveTwo, moveThree):
        self.name = name.title()
        self.health = health
        self.damage = damage
        classList.append(self)
        self.moveOne = moveOne
        self.moveTwo = moveTwo
        self.moveThree = moveThree
        self.classMoveList = [moveOne, moveTwo, moveThree]

    def __repr__(self):
        description = "{name}: {health} health | {damage} damage".format(name=self.name, health=self.health, damage=self.damage)
        return description

    def getName(self):
        return self.name

# ================FUNCTIONS================================FUNCTIONS================================FUNCTIONS===========
# Special Functions

# prints a numbered version of the list, for better user experience
def numberedList(listList):
    for number, item in enumerate(listList):
        print(number + 1, item)

# catches string-to-integer problems before they crash the game. Almost all input is through integers, so almost all input should pass through this function to ensure no errors.
def inputInt(userInput):
    try:
        # tries to turn user input into an int
        intPut = int(userInput)
        return intPut
    except:
        # if int() fails, just sets the int to 0 to be handled by the function that originally called inputInt()
        print("Error - Input not a number. Defaulted to 1")
        intPut = 1
        return intPut

# Checks to make sure the number chosen is actually within the list range, and subtracts 1 to select the correct option.
# Otherwise, it returns 0 to keep the game going.
def inputRange(userInput, listToCheck):
    if userInput <= len(listToCheck):
        return userInput -1
    else:
        print("Error - Chosen number out of range, defaulted to 1")
        return 0


#-----------------------------------------------------------------------------------------------------------------------
# Combat Functions

#Keeps track of player score
class PlayerScore:
    playerScore = 0

    def __init__(self):
        self.playerScore = 0

    def __repr__(self):
        return self.playerScore

    def getData(self):
        return self.playerScore

    def reset(self):
        self.playerScore = 0

    def add(self, scoreToAdd):
        self.playerScore += scoreToAdd

    def subtract(self, scoreToSubtract):
        self.playerScore -= scoreToSubtract

playerScore = PlayerScore()


# Asks the player to choose which enemy they would like to attack, as well as displaying their current stats with __repr__()
def enemyChoicebox():
    print("Choose which enemy to attack! \n" + playerOne.__repr__())
    numberedList(creatureList)
    enemyChoice = inputInt(input())
    if enemyChoice > 0 and enemyChoice <= len(creatureList):
        enemy = creatureList[enemyChoice -1]
    else:
        enemy = creatureList[0]
    return enemy

# Asks the player to choose which move to use, as well as displaying their current stats with __repr__()
def moveChoicebox():
    moveList = playerOne.playerMoveList
    print("-----------------------------------------------------------------------------------------------------------")
    numberedList(creatureList)
    print("-----------------------------------------------------------------------------------------------------------")
    msg = "Choose your attack! \n" + playerOne.__repr__()
    print(msg)
    currentScore = playerScore.getData()
    print("Your score is: ", currentScore)
    numberedList(moveList)
    moveChoice = inputInt(input())
    playerOne.attackMoves(moveChoice)

# The PC chooses which creature will attack, as long as there are creatures still alive.
def enemyMove():
    if len(creatureList) > 0:
        attackingCreature = random.choice(creatureList)
        attackingCreature.attack()

# Displays success message
def youWon():
    global wavesCompleted
    wavesCompleted +=1
    currentScore = playerScore.getData()
    print("()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----")
    print("Your score is: ", currentScore)
    print("Wave {wavenum} completed!".format(wavenum = wavesCompleted))
    print("You have triumphed against the creatures!")
    print("Press 1 to continue playing, press any key to exit")
    print("()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----()----")
    continuePlaying = inputInt(input())
    if continuePlaying == 1:
        creatureList = []
        playerOne.playerHealthPotion()
        newBattlefield()
        attackLoop()
    else:
        exit()

# Displays game over message
def gameOver():
    currentScore = playerScore.getData()
    print("===========================================================================================================")
    print("Your score is: ", currentScore)
    print("You completed {wavenum} waves".format(wavenum = wavesCompleted))
    print("You have been defeated. Your strength was inadequate and our world will plunge into chaos...")
    print("===========================================================================================================")

#-----------------------------------------------------------------------------------------------------------------------
# Character Creator
def characterCreator():
    # Asks the player for a name and which class they would like to play as

    #These are unused variables but I'm not ready to delete them yet
    characterName = "Eravor"
    nameLabel = "Eravor"
    characterClass = "Duelist"
    characterCreatorMessage = """
	CREATURE GLADIATOR

	Choose the name of your gladiator!
	"""

    # Enter your name, choose your class, prepare to fight!
    print("___Character Creator___")
    # Asks for a name. This input is not protected because the name does not matter at all, so any input is valid.
    nameChoice = input("Character Name: ")

    # Prints the class list
    print("CHOOSE YOUR CLASS!")
    numberedList(classList)

    # Asks for input, and then sets the playerClass accordingly
    classChoice = inputInt(input("Class:   "))
    classChoice = inputRange(classChoice, classList)
    playerClass = classList[classChoice]
    # Creates the playerOne object based on user choices.
    global playerOne
    playerOne = Player(nameChoice, playerClass)


#-----------------------------------------------------------------------------------------------------------------------
# Enemy Generator
creatureList = []
deadCreatureList = []
# Generates names. This is an incredibly useful part of the program which I need to save for future projects
# returns the name as a string
def nameGenerator():
    vowel = ["a", "e", "i", "o", "u", "ai", "au", "ea", "ee", "ei", "eo", "eu", "ie", "oa", "oe", "oo", "ou", "ue", "ui"]
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
                 "th", "sh", "ch", "bl", "br", "cl", "cr", "dr", "fl", "fr", "gl", "gr", "pl", "pr", "qu", "sc", "sk",
                 "sl", "sm", "sn", "sp", "st", "sw", "tr","tw", "ck", "gh", "kn", "mb","ng","ph","wh", "wr"]
    nameList = []

    #first, generate the length of the name
    nameLength = random.randint(1, 2)
    #then, flip a coin to start with a vowel or consonant
    vowelFirst = random.choice([True, False])
    #Then, alternate between vowels and consonants using a for loop and append them to the list
    if vowelFirst:
        nameList.append(random.choice(vowel))
    for letter in range(nameLength):
        nameList.append(random.choice(consonant))
        nameList.append(random.choice(vowel))

    #Finally,  join the list into one single string in title case
    generatedName = "".join(nameList)
    return generatedName.title()

#picks a random class from the enemyClassList
def classPicker():
    enemyClass = random.choice(enemyClassList)
    return enemyClass

def createCreature():
    creatureName = nameGenerator()
    creatureClass = classPicker()

    return Creature(creatureName, creatureClass)


def newBattlefield():
    #Save these creatures for boss battles or something
    # creature1 = Creature("Gorgon", mauler)
    # creature2 = Creature("Zevenexus Qi-Zor", lichDemon)
    # creature3 = Creature("Zeb Zegox", erzogSwine)
    creature1 = createCreature()
    creature2 = createCreature()
    creature3 = createCreature()
    global creatureList
    creatureList = [creature1, creature2, creature3]

#-----------------------------------------------------------------------------------------------------------------------
# the actual gameplay loop
def attackLoop():
    # Housekeeping:
    global playersTurn # Make sure the playersTurn is accessible from anywhere in the program. VERY IMPORTANT
    playersTurn = True # At the beginning of the loop, make it the players turn.

    global creatureList

    # Start the players turn loop
    while not playerOne.isDead and playersTurn and len(creatureList) > 0:
        moveChoicebox()
        # time.sleep() prevents freshly killed creatures from landing blows on the player. The computer was getting ahead of itself
        time.sleep(1)

    # Start the enemies' turn loop
    while len(creatureList) > 0 and not playersTurn and not playerOne.isDead:
        enemyMove()
        time.sleep(1)

    if not len(creatureList):
        # If all the creatures are dead,
        youWon()

    elif playerOne.isDead:
        # if you are dead,
        gameOver()
    else:
        # If no one has won, keep looping through the game!
        attackLoop()


#-----------------------------------------------------------------------------------------------------------------------
# intro Message box
def introMessage():
    # An intro message explaining how to play the game
    beginMsg = """
	WELCOME TO CREATURE GLADIATOR

	The great and evil wizard, Akozuto, is using blood magic to create twisted and mangled creatures. YOU MUST STOP HIM!
	====================================================================================================================
	Try to beat as many waves of Akozuto's creatures as you can!
	
	First, create your character and choose a class! Each class has a different amount of health, and does a different
	amount of damage.
	Each class has three moves:
	    1. A direct damage attack. You choose a single creature to attack, using all of your might
	    2. An area attack. This attacks all enemies on the battlefield, but isnt as powerful.
	    3. This blocks all damage for the next turn
	
    Make a selection by entering the number of your choice, and then pressing 'enter'.
    ====================================================================================================================
	"""

    print(beginMsg)


#------------------ENEMY CLASS LIST------------------ENEMY CLASS LIST------------------ENEMY CLASS LIST-----------------
#class list to initialize all enemy class types
#Class list for enemy classes
enemyClassList = []

#create classes here!
#EnemyClass("Name", health, damage, stab, slash, block)
mauler = EnemyClass("Mauler", 10, 60, "Bite", "Claw-Swipe", "Low Guard")
lichDemon = EnemyClass("Lich Demon", 70, 40, "Bone Remover", "Soul-Tear", "Gravestone")
erzogSwine = EnemyClass("Erzog-Swine", 30, 40, "Head-Butt", "Hill-Roller", "Mud-Wall")
flameSphynx = EnemyClass("Flame Sphynx", 40, 80, "Burning Eyes", "Conflagration", "Incinerator Shield")
ratSoldier = EnemyClass("Rat Soldier", 50, 30, "Sword-Stab", "Tail Whip", "Shield-Bash")
bearPaladin = EnemyClass("Bear Paladin", 80, 30, "Light-Blade", "Sun-Beam", "Armor of Erzog")


# ----------------CLASS LIST------------CLASS LIST-------------CLASS LIST--------------CLASS LIST------------CLASS LIST-
# class list to save all classes in
classList = []

# create classes here!
# PlayerClass("Name", health, damage, stab, slash, block)
duelist = PlayerClass("Duelist", 65, 55, "Lunge", "Drawcut", "Parry")
mage = PlayerClass("Mage", 90, 30, "Lightning Fingers", "Fireblast", "Ward")
warrior = PlayerClass("Warrior", 80, 40, "Hack", "Tear Asunder", "Shield Block")
sorceror = PlayerClass("Sorcerer", 50, 70, "Banish", "Meteoric Rain", "Teleport")
swordsman = PlayerClass("Swordsman", 70, 50, "Stab", "Slash", "Block")
druid = PlayerClass("Druid", 85, 35, "Spider Venom", "Poison Gas", "Staff Block")

# ======================================================================================================================
# -----------------BEGIN!-----------------BEGIN!-----------------BEGIN!-----------------BEGIN!-----------------BEGIN!---
# ======================================================================================================================
wavesCompleted = 0

#plays introMessage.
introMessage()

# Game begins, you must create your character!
characterCreator()




# Ready, FIGHT!
newBattlefield()
attackLoop()



# ======================================================================================================================
# CREATURE GLADIATOR
#
# Written by Joe Doherty
# July 2022