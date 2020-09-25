import pandas as pd 
import numpy as np 

def score_func(row):
  ba = row.BA 
  bid = row.Bid 
  result = row.Result
  if ba == 'y' and result == bid:
    score_col = bid * 10
  elif ba == 'y':
    score_col = bid * -10
  elif result >= bid:
    score_col = bid * 3 + result - bid
  else:
    score_col = bid * -3
  return score_col

class Player():
  def __init__(self, name):
    self.name = name
    self.bids = pd.DataFrame(columns=['Round #', 'Card Count', 'Player', 'Bid', 'BA', 'Result'])

  def __repr__(self):
    repr = f'{self.name}'
    return repr
  
  def bid(self, round_number, card_count):
    round_data = {
      'Round #': [round_number],
      'Card Count': [card_count],
      'Player': str(self.name),
      'Result': np.NaN
    }
    print(f'What does {self.name} bid?')
    round_data['Bid'] = int(input())
    if round_data['Bid'] == card_count:
      print('Backalley?')
      round_data['BA'] = str(input())
    else:
      round_data['BA'] = 'n'
    bid_df = pd.DataFrame(round_data)
    self.bids = pd.concat([self.bids, bid_df])
    return bid_df
  
  def score_round(self):
    print(f'How many tricks did {self.name} win?')
    result = int(input())
    self.bids.fillna(result, inplace=True)
    self.score = self.bids.copy()
    self.score['Score'] = self.score.apply(score_func, axis=1)
    self.score = self.score.loc[:, ['Round #', 'Card Count', 'Player', 'Score']]
    return self.score

class Game():
  def __init__(self, names):
    self.players = names
    self.names = [print(i) for i in names]
    self.max_hand = (54 - len(names) % 54) / len(names)
    self.round_number = 1
    self.count = 1
    self.ascending = True

  def card_count(self):
    if self.count < self.max_hand:
        self.ascending = True
        self.count += 1
    else:
        self.ascending = False
        self.count += -1

  def change_order(self):
    new_list = self.players[1:]
    new_list.append(self.players[0])
    return new_list

  def bid(self):
    bid_list = []
    for name in self.players:
      bid = name.bid(self.round_number, self.count)
      bid = bid.loc[:, [c for c in bid.columns if c != 'Result']]
      bid_list.append(bid)
    bid = pd.concat(bid_list)
    bid.sort_values(by='Bid', inplace=True, ascending=False)
    self.round_number += 1
    self.card_count()
    return bid.reset_index(drop=True)
  
  def score(self):
    scores = []
    for player in self.players:
      score_df = player.score_round()
      scores.append(score_df)
    scores = pd.concat(scores)
    scores = scores.groupby('Player').Score.sum()
    scores.sort_values(ascending=False)
    self.players = self.change_order()
    return scores