#
#
#
#
#        <=========]==O    CREATURE
#   (\)_(/)           GLADIATOR
# ======================================================================================================================
# WELCOME TO CREATURE GLADIATOR
# The great and evil wizard, Akozuto, is using blood magic to create
# twisted and mangled creatures. YOU MUST STOP HIM!
#
import random
from easygui import *
from appJar import gui


print("WELCOME TO CREATURE GLADIATOR")


#
# -----------AVAILABLE CLASSES----------
# Duelist: Uses a rapier. High damage, low health
# Mage: Uses magic to stay alive. Low damage, high health.
# ==========CLASSES=====================CLASSES=====================CLASSES=====================CLASSES=================
# defines the player class
class Player:
    name = ""
    fighterClass = ""
    health = 0
    damage = 0
    isBlocking = False
    isDead = False

    # initiates a new player with all of their information
    def __init__(self, name, fighterClass):
        self.name = name
        self.fighterClass = fighterClass
        self.health = fighterClass.health
        self.damage = fighterClass.damage

    # Player character description box
    def __repr__(self):
        description = "{name} : {fighterClass} : {health} health : {damage} damage".format(name=self.name, fighterClass=self.fighterClass.name, health=self.health, damage=self.damage)
        return description

    # Returns the name of the player character as a string
    def getName(self):
        return self.name

    # Returns the class name of the player character as a string
    def getClass(self):
        return fighterClass

    # Method for damaging the player character
    def damagePlayer(self, damage):
        if playerOne.isBlocking:
            msgbox("{name} blocked the attack!".format(name = self.name))
        elif not playerOne.isBlocking:
            self.health -= damage
            self.checkIfDead()


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


    # creature description box
    def __repr__(self):
        description = "{name} : {creatureClass} | Damage: {damage}| Health: {health}|{classHealth} ".format(name=self.name, creatureClass=self.creatureClass.name, health=self.health, damage=self.damage, classHealth = self.creatureClass.health)
        return description


    # check if health has reached 0
    def checkIfDead(self):
        if (self.health <= 0):
            self.isDead = True
            creatureList.remove(self)


    # method for damaging the creature
    def damageCreature(self, damage):
        self.health -= damage
        damageMsg = "you did {damage} to {name}".format(damage = damage, name=self.name)
        msgbox(damageMsg, damageMsg)
        self.checkIfDead()
        if (self.isDead):
            deadMsg = "{name} has been slain!".format(name=self.name)
            msgbox(deadMsg, deadMsg)

    # method to return the name of the creature
    def getName(self):
        return self.name

    def getClass(self):
        return self.creatureClass

    # method to attack the player
    def attack(self):
        playerOne.damagePlayer(self.damage)
        msgbox("{creature} attacked {player} for {damage} damage!".format(creature = self.name, player = playerOne.getName(), damage = self.damage))


#-----------------------------------------------------------------------------------------------------------------------
# Enemy Classes, eventually to be chosen at random by the PC
class EnemyClass:
    name = "Slime"
    health = 10
    damage = 10
    moveOne = ""
    moveTwo = ""
    moveThree = ""

    def __init__(self, name, health, damage, moveOne, moveTwo, moveThree):
        self.name = name.title()
        self.health = health
        self.damage = damage
        enemyClassList.append(self)
        self.moveOne = moveOne
        self.moveTwo = moveTwo
        self.moveThree = moveThree
        self.enemyMoveList = [moveOne, moveTwo, moveThree]

    def __repr__(self):
        description = "".format(health=self.health)
        return description

    def getName(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------
# These are classes that a player can choose from in the beginning of the game
class PlayerClass:
    name = "Wimp"
    health = 10
    damage = 10
    moveOne = ""
    moveTwo = ""
    moveThree = ""

    def __init__(self, name, health, damage, moveOne, moveTwo, moveThree):
        self.name = name.title()
        self.health = health
        self.damage = damage
        classList.append(self)
        self.moveOne = moveOne
        self.moveTwo = moveTwo
        self.moveThree = moveThree
        self.playerMoveList = [moveOne, moveTwo, moveThree]

    def __repr__(self):
        description = "{name}: {health} health | {damage} damage".format(name=self.name, health=self.health,
                                                                         damage=self.damage)
        return description

    def getName(self):
        return self.name

    def attackMoves(self, moveNum):
        playerOne.isBlocking = False

        # attack One is a simple single-enemy attack, like stab
        def attackOne(self):
            damage = playerOne.damage
            enemyChoice = enemyChoicebox()
            if not enemyChoice == goBack:
                print("skipped the if statement")
                enemyChoice.damageCreature(damage)

        # attack Two is an area-of-effect attack, like slash
        def attackTwo(self):
            damage = self.damage / 3
            for creature in creatureList:

                creature.damageCreature(damage)

        # attack Three is a block of some kind, like parry
        def attackThree(self):
            # damage next turn is zero
            playerOne.isBlocking = True

        if moveNum == 0:
            attackOne(self)
        elif moveNum == 1:
            attackTwo(self)
        else:
            attackThree(self)


#-----------------------------------------------------------------------------------------------------------------------
#Special Command classes for special choices in lists
class GoBack:
    name = "Go Back"

    def method(self):
        moveChoicebox()

    def __repr__(self):
        description = "Go back to previous screen"
        return description

# ================FUNCTIONS================================FUNCTIONS================================FUNCTIONS===========
#-----------------------------------------------------------------------------------------------------------------------
# Special Command functions
def specialCommandFinder(selectedChoice):
    index = 0
    for item in specialCommandsList:
        if selectedChoice == item.__repr__():
            item.method()
            break
        index += 1
    return False


#-----------------------------------------------------------------------------------------------------------------------
# Combat functions
def enemyChoicebox():
    enemyChoice = choicebox("Choose which enemy to attack! \n" + playerOne.__repr__(), "Choose which enemy to attack!", creatureList + specialCommandsList)
    enemy = enemyFinder(enemyChoice)
    return enemy

def moveChoicebox():
    msg = """Choose your attack!
        Health: {health}|{classHealth}
    """.format(health = playerOne.health, classHealth = playerOne.fighterClass.health)

    moveChoice = choicebox(msg, "Choose your attack!", playerOne.fighterClass.playerMoveList)
    moveFinder(moveChoice)

def moveFinder(moveChoice):
    index = 0
    for move in playerOne.fighterClass.playerMoveList:
        if moveChoice == move:
            playerOne.fighterClass.attackMoves(index)
            break
        index += 1

def enemyFinder(enemyChoice):
    index = 0

    for enemy in creatureList:
        if enemyChoice == enemy.__repr__():
            print(enemy)
            return enemy
            break
        index += 1
        if index >= len(creatureList):
            specialCommandFinder(enemyChoice)

def classFinder(classChoice):
    for charClass in classList:
        if charClass.__repr__() == classChoice:
            return charClass

def enemyMove():
    if len(creatureList) > 0:
        attackingCreature = random.choice(creatureList)
        if attackingCreature.checkIfDead():
            attackingCreature.attack()
    else: return

def youWon():
    msgbox("You have triumphed against the creatures!", "You Win", ok_button="Join the Celebration")

def gameOver():
    msgbox("You have been defeated. Your strength was inadequate and our world will plunge into chaos...", "Game Over",
           ok_button="Concede Defeat")

#-----------------------------------------------------------------------------------------------------------------------
# Character Creator
def characterCreator():
    characterName = "Eravor"
    characterClass = "Duelist"
    characterCreatorMessage = """
	CREATURE GLADIATOR

	Choose the name of your gladiator!
	"""

    nameLabel = "Eravor"
    nameChoice = enterbox(characterCreatorMessage, "Character Creator", nameLabel)
    classChoice = choicebox("CHOOSE YOUR CLASS!", "Choose your Class", classList)

    classChoice = classFinder(classChoice)

    characterName = nameChoice
    characterClass = classChoice

    global playerOne
    playerOne = Player(characterName, characterClass)


#-----------------------------------------------------------------------------------------------------------------------
# the actual gameplay loop
def attackLoop():
    while len(creatureList) and not playerOne.isDead:
        moveChoicebox()
        enemyMove()

    if not len(creatureList):
        youWon()
    elif playerOne.isDead:
        gameOver()
    else:
        msgbox("GAME OVER")


#-----------------------------------------------------------------------------------------------------------------------
# into Message box
def introMessage():
    beginMsg = """
	WELCOME TO CREATURE GLADIATOR

	The great and evil wizard, Akozuto, is using blood magic to create twisted and mangled creatures. YOU MUST STOP HIM! {name}, you are a powerful {charClass}. You are the only thing protecting our world from the terrible hoarde of Akozuto!
	Will you do what is necessary to protect our world?
	""".format(name=playerOne.name, charClass=playerOne.fighterClass.name)

    if (ynbox(beginMsg) == False):
        exit()


#----------------SPECIAL COMMANDS LIST----------------SPECIAL COMMANDS LIST----------------SPECIAL COMMANDS LIST--------
# Initialize special commands here
goBack = GoBack()

#------------------ENEMY CLASS LIST------------------ENEMY CLASS LIST------------------ENEMY CLASS LIST-----------------
#class list to initialize all enemy class types
#Class list for enemy classes
enemyClassList = []

#create classes here!
#EnemyClass("Name", health, damage, stab, slash, block)
mauler = EnemyClass("Mauler", 30, 70, "Bite", "Claw-Swipe", "Low Guard")
lichDemon = EnemyClass("Lich Demon", 80, 20, "Bone Remover", "Soul-Tear", "Gravestone")
erzogSwine = EnemyClass("Erzog-Swine", 50, 50, "Head-Butt", "Hill-Roller", "Mud-Shield")
flameSphynx = EnemyClass("Flame Sphynx", 10, 90, "Burning Eyes", "Conflagration", "Incinerator Shield")
ratSoldier = EnemyClass("Rat Soldier", 80, 20, "Sword-Stab", "Tail Whip", "Shield-Block")
bearPaladin = EnemyClass("Bear Paladin", 90, 10, "Light-Blade", "Sun-Beam", "Armor of Erzog")


# ----------------CLASS LIST------------CLASS LIST-------------CLASS LIST--------------CLASS LIST------------CLASS LIST-
# class list to save all classes in
classList = []

# create classes here!
# PlayerClass("Name", health, damage, stab, slash, block)
duelist = PlayerClass("Duelist", 70, 30, "Lunge", "Drawcut", "Parry")
mage = PlayerClass("Mage", 80, 20, "Lightning Fingers", "Fireblast", "Ward")
warrior = PlayerClass("Warrior", 60, 40, "Hack", "Tear Asunder", "Shield Block")
sorceror = PlayerClass("Sorcerer", 20, 80, "Banish", "Meteoric Rain", "Teleport")
swordsman = PlayerClass("Swordsman", 50, 50, "Stab", "Slash", "Block")
druid = PlayerClass("Druid", 90, 10, "Spider Venom", "Poison Gas", "Staff Block")
#------------------ENEMY LIST------------------ENEMY LIST------------------ENEMY LIST------------------ENEMY LIST-------

creature1 = Creature("Gorgon", mauler)
creature2 = Creature("Zevenexus Qi-Zor", lichDemon)
creature3 = Creature("Zeb Zegox", erzogSwine)

creatureList = [creature1, creature2, creature3]
specialCommandsList = [goBack]


# ======================================================================================================================
# -----------------BEGIN!-----------------BEGIN!-----------------BEGIN!-----------------BEGIN!-----------------BEGIN!---
# ======================================================================================================================

characterCreator()

#plays introMessage. Toggle with #
#introMessage()

attackLoop()

# ===========FIGHT===============
