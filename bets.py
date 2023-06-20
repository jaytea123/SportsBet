import random


MINIMUM_BALANCE = 100


def get_balance(player_balance):
  return player_balance

def deposit(player_balance, deposit_amount):
  player_balance += deposit_amount
  return player_balance

def withdrawl(player_balance, withdrawl_amount):
  if withdrawl_amount <= (player_balance - MINIMUM_BALANCE):
    player_balance -= withdrawl_amount
    return player_balance
  else:
    withdrawl_amount = player_balance - MINIMUM_BALANCE
    player_balance = 100
    print('Minimum balance is $100, withdrawing $',withdrawl_amount)
    return player_balance

def get_user_bet(num_bets, player_balance, bet_amount, team, game):
  return 1

def get_payout(team, t1_odds, t2_odds, bet_amount):
  if team == 1:
    #Use team1 odds
    if t1_odds >= 0:
      payout = bet_amount * (t1_odds / 100)
    else:
      payout = bet_amount / (t1_odds / 100) * -1

  else:
    #Use team2 odds
    if t2_odds >= 0:
      payout = bet_amount * (t2_odds / 100)
    else:
      payout = bet_amount / (t2_odds / 100) * -1
      
  return payout
  

def winning_bet(t1, t2, o1, o2):

  #Positive Probability = 100 / (odds + 100)
  if o1 >= 0:
    t1_probability = 100 / (o1 + 100)
  #Negative Probability = (-1 * odds) / ((-1 * odds) + 100)
  else:
    t1_probability = (-1 * o1) / ((-1 * o1) + 100)

  if o2 >= 0:
    t2_probability = 100 / (o2 + 100)
  else:
    t2_probability = (-1 * o2) / ((-1 * o2) + 100)

  
  
  team_list = [t1,t2]
  #print('o1: ', t1_probability, 'o2: ', t2_probability)
  result = random.choices(team_list, weights=(t1_probability, t2_probability), k=1)
  return str(result[0])

