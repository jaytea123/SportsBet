import random

class Games:
  def __init__(self, i, t1, t2):
    self.i = i
    self.bet = False
    self.bet_amount = 0
    self.team_picked = t1
    self.team1 = t1
    self.team2 = t2
    self.winner = ''
    self.payout = 0
    self.t1odds = 0
    self.t2odds = 0

  def __str__(self):
    return f"{self.team1}{self.team2}"


class Team():
  def __init__(self, i):
    self.i = i
    self.name = ''
    self.odds = 1
    
  def team_odds():
    return(random.randint(-600,600))