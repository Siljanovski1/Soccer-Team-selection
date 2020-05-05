#!/usr/bin/env python
# coding: utf-8

# In[ ]:


players = []

add_players = input("Would you like to add players to the team ? \n(yes/no) ")
while add_players.lower() =="yes":
    name = input("Enter the players name : ")
    players.append(name)
    add_players = input("Would you like to add another player ? \n(yes/no) ")
print("\nThere are {} players added to the list !".format(len(players)))

players_number = 1
for player in players:
    print("Player: {},{} !".format(players_number,player))
    players_number += 1
        
goalkeeper = input("Please select the goalkeeper from the list 1 ~ {} ?".format(len(players)))
goalkeeper = int(goalkeeper)

print("The goalkeeper is: {} !".format(players[goalkeeper -1]))

