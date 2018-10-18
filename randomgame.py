''' to create game from random numbers
    there will be two players player A and Player B
    Player A will throw dice and get number similary player b will throw dice and get number
    depends on total score after n number of tries say -10, players whose score is max wins the game
'''
from random import *
import time
player1 = input("PLAYER 1 NAME")
player2 = input("PLAYER 2 NAME")
numberoftimes = 10 #input("Enter number of tries you want to play with apponent")
dice=[1,2,3,4,5,6]
counter =1
player1totalscore = 0
player2totalscore = 0
while(counter<=numberoftimes):
    counter=counter+1
    player1dice= sample(dice,1)
    #print(type(player1dice))
    time.sleep(2)
    print(player1 , " throws dice and number is  ",player1dice)
    player1totalscore = player1totalscore + int(player1dice[0])
    player2dice = sample(dice,1)
    time.sleep(2)
    print(player2, " throws dice and number is  ", player2dice)
    player2totalscore = player2totalscore + int(player2dice[0])

print("player 1 As --> {0} score is {1}  \n and player 2 As --> {2} score is {3} ".format(player1,player1totalscore,player2,player2totalscore))
if player1totalscore >player2totalscore:
    print("Hurry !!! {0} wins match ".format(player1))
elif player1totalscore < player2totalscore:
    print("Hurry !!! {0} wins match ".format(player2))
else:
    print(" MATCH DRAW .. GOOD PLAY BY BOTH TEAMS")