print("BANK!")
numRounds = input("Select the number of rounds you would like to play: 10, 15, or 20:\n")
numRounds = int(numRounds)

#check for valid number of rounds input
while numRounds not in [10, 15, 20]:
    numRounds = int(input("Please enter a valide number of rounds. You can play 10, 15, or 20 rounds:\n"))

print("You selected", numRounds, "Rounds!")

numPlayers = int(input("How many people will be playing? The minimum number of players is 2.\n"))

#check for valid number of players input
while numPlayers < 2:
    numPlayers = int(input("Please enter a valid number of players:\n"))

#make player object list
print("Please enter each player's name:\n")
players = []

#Initialize roundTotal values and rollVal totals
roundTotal = 0
rollVal = 0

#Player object
class Player:
    name = ""
    playerNumber = 0
    points = 0
    status = 0
    rollVal = 0
    def __init__(self, name, playerNumber):
        self.name = name
        self.playerNumber = playerNumber #use to keep track of turns or identify player who wants to bank?
        points = 0 # points players accumulate during the game
        status = 0 # 0 = still playing, 1 = they have banked

    def __str__(self):
        return f"{self.playerNumber} {self.name} | {self.points}"

#Method for banking points
def Bank():
    isValid = False
    print("Select which player would like to bank by entering the player number. Press 'r' to return to gameplay:\n")
    
    #list out players
    playersListTemp = []
    for player in players: 
        playersListTemp.append(int(player.playerNumber))
        print(player)
        
    #Check user input for validity
    userInput = input("Enter number of player who wants to bank: ")
    while not isValid:
        if userInput.isdigit():
            temp = int(userInput)
            if temp not in playersListTemp:
                isValid = False
                userInput = input("Please enter a valid player number:\n")
            else:
                
                players[temp].points += roundTotal
                for player in players:
                    print(player)
                isValid = True
        elif userInput == "r":
            isValid = True
            return

#Get user input for number of players and names of players
for x in range(numPlayers):
    #print("Player", str(x))
    playerNumTemp = x
    playerName = input("Player " + str(x + 1) + ": ")

    playerNum = playerNumTemp

    #create new player object
    player = Player(playerName, playerNum)

    players.insert(playerNum, player)
    playerName = "temp"



for x in range(numRounds):
#Start the game: method PlayGame()

    for x in range(3):
        print("Current score:", roundTotal)
        rollVal = int(input("2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\n"))
        #check for valid roll input
        while rollVal not in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            rollVal = int(input("Please enter a valid roll value:\n"))

        if rollVal == 7:
            roundTotal += 70
        elif rollVal == 1:
            Bank()
        else:
            roundTotal += rollVal
    while roundTotal > 0:
        print("Current score:", roundTotal)
        rollVal = int(input("2, 3, 4, 5, 6, *7*, 8, 9, 10, 11, 0(if doubles are rolled) or 1 to bank!\n"))
        if rollVal == 7:
            roundTotal = 0
            print("Round total = 0!")
            print(roundTotal)
            break
        elif rollVal == 0:
            roundTotal *= 2
        elif rollVal == 1:
            Bank()
        else:
            roundTotal += rollVal



        
