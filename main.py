### Program for placing NBA money line bets, both single bets, multiple single bets, and parlay bets ###

import games
import random
import bets


TEAMS_LIST = ['76ers','Bucks','Bulls','Cavaliers','Celtics','Clippers',
'Grizzlies','Hawks','Heat','Hornets','Jazz','Kings','Knicks','Lakers','Magic',
'Mavericks','Nets','Nuggets','Pacers','Pelicans','Pistons','Raptors',
'Rockets','Spurs','Suns','Thunder','Timberwolves','Trailblazers','Warriors','Wizards']

TEAMS_PER_GAME = 2

NUM_TEAMS = len(TEAMS_LIST)
NUM_GAMES = int(NUM_TEAMS / 2)

player_balance = 100
bets_placed = 0

  

#instantiate all 30 instances of the Teams object
all_teams = {}
for i in range(NUM_TEAMS):
  all_teams[i] = games.Team(i)
  all_teams[i].name = TEAMS_LIST[i]
  all_teams[i].odds = games.Team.team_odds()
  
#Shuffle order of the teams to ensure different matchups each time
random.shuffle(all_teams)

#Instantiate the 15 instances of the Games object
all_games = {}
j = 0
for i in range(NUM_GAMES):
  all_games[i] = games.Games(i, all_teams[j].name, all_teams[j+1].name)
  print('Game',i+1,': ')
  print()
  print(all_games[i].team1, all_games[i].team2)

  #Make sure the odds are positive for one team and negative for the other
  if(((all_teams[j].odds > 0) and (all_teams[j+1].odds > 0)) or 
     ((all_teams[j].odds < 0) and (all_teams[j+1].odds < 0))):
       all_teams[j].odds *= -1

  all_games[i].t1odds = all_teams[j].odds
  all_games[i].t2odds = all_teams[j+1].odds
  print(all_teams[j].odds, all_teams[j+1].odds)
  print()
  
  j += 2

#Display user balance
print()
print('Balance: $', bets.get_balance(player_balance))
print()

#Get user input:
# 1 - Deposit
# 2 - Withdraw
# 3 - Bet
while True:
  print('What would you like to do?')
  print('1 - Deposit')
  print('2 - Withdraw')
  print('3 - Bet')
  print('4 - Exit')

  try:
    user_choice = int(input())
    
    if (user_choice != 1) and (user_choice != 2) and (user_choice != 3) and (user_choice != 4):
      print('Must enter a number between 1 - 4')
      print()
      continue
  except:
    print('Must enter a number between 1 - 4')
    print()
  else:
    if user_choice == 1:
      #Deposit
      while True:
        print('Please enter the amount you would like to deposit: ')
    
        try:
          deposit_amount = int(input())
          if deposit_amount > 0:
            player_balance = bets.deposit(player_balance, deposit_amount)
            print('You deposited $', deposit_amount)
            print('Your new balance is: $', player_balance)
            print()
            break
          else:
            print('Must enter a positive integer')
        except:
          print('Must enter a positive integer')
    elif user_choice == 2:
      #Withdrawl
      while True:
        print('Please enter the amount you would like to withdraw: ')
    
        try:
          withdrawl_amount = int(input())
          
        except:
          print('Must enter a positive integer')
        else:
          if withdrawl_amount > 0:
            player_balance = bets.withdrawl(player_balance, withdrawl_amount)
            if player_balance > 100:
              print('You withdrew $', withdrawl_amount)
            print('Your new balance is: $', player_balance)
            print()
            break
          else:
            print('Must enter a positive integer')
    elif user_choice == 3:
      #Bet
      #1 - Which games they want to bet on
      for i in range(NUM_GAMES):
        print('Do you wish to bet on game ', i + 1)
        print(all_games[i].team1, ' vs ', all_games[i].team2)
        print('1 - Yes')
        print('2 - No')
    
        while True:
          try: 
            x = int(input())
          except:
            print('Must enter either 1 or 2')
          else:
            if x == 1:
              all_games[i].bet = True
              bets_placed += 1
              break
            elif x == 2:
              all_games[i].bet = False
              break
            else:
              print('Must enter either 1 or 2')
              continue
    
        #If they wish to bet on this game, get which team they want to bet on
        #Then get the amount they wish to bet on that team
        if all_games[i].bet == True:
          while True:
            print('Which team would you like to bet on?')
            print('1 - ', all_games[i].team1)
            print('2 - ', all_games[i].team2)
            try:
              x = int(input())
            except:
              print('Exception: Must enter either a 1 or 2')
            else:
              if x == 1 or x == 2:
                  all_games[i].team_picked = x
                  #Get amount they wish to bet
                  while True:
                    print('Enter the amount (in USD) that you would like to bet: ')
                    #Check to see if they entered a number
                    try:
                      all_games[i].bet_amount = int(input())
                    except:
                      print('Must enter a number only')
                    else:
                      #Check to see if they have enough money to make that bet
                      if all_games[i].bet_amount > player_balance:
                        all_games[i].bet_amount = 0
                        print('Amount wished to bet exceeded your balance of ', player_balance)
                        print('You may only bet up to your current balance')
                      #If bet_amount is less than or equal to player_balance
                      #calculate payout, and ask them to confirm
                      else:
                        all_games[i].payout = bets.get_payout(all_games[i].team_picked, all_games[i].t1odds,           
                        all_games[i].t2odds, all_games[i].bet_amount)
                        player_balance -= all_games[i].bet_amount
                        print()
                        print('Team Picked: ', all_games[i].team_picked)
                        print('Amount Wagered: $', all_games[i].bet_amount)
                        print('Potential Payout: $', all_games[i].payout)
                        print('Remaining Balance: $', player_balance)
                        print()
                        break
              else:
                print('Must enter either a 1 or 2')
                continue
              break
                
          else:
            print('Must enter either a 1 or 2')  
  
      #Simulate Games
      j = 0
      for i in all_games:
        all_games[i].winner = bets.winning_bet(all_teams[j].name,all_teams[j+1].name,all_teams[j].odds,all_teams[j+1].odds)
        print('Game ',i + 1, 'winner: ', str(all_games[i].winner))
        j += 2
        #If player bet on that game, determine winnings/losses
        if all_games[i].bet == True:
          #Determine if they won or lost
          if all_games[i].team_picked == 1:
            all_games[i].team_picked = all_games[i].team1
            #Add winnings to balance, including original wager
          else:
            all_games[i].team_picked = all_games[i].team2

          print(all_games[i].team_picked)
          if all_games[i].team_picked == all_games[i].winner:
            player_balance = player_balance + all_games[i].payout + all_games[i].bet_amount
            print('You Won! New Balance: $', player_balance)
          else:
            print('Bummer')
            #If lost, nothing needs to happen as they already had the money deducted
            #Update and display balance

      continue

    #Exit
    else:
      print('Thank you for playing, come back soon!')
      print('Disclaimer: If you or someone you know is suffering from an addiction to gambling, please call 1-800-522-4700')
      break;
  