import pandas as pd 
import numpy as np 
def change_order(ls):
    first = ls[0]
    new_list = ls[1:]
    new_list.append(first)
    return new_list

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

def card_count(*args):
    count = 0
    ascending = True
    if count < max_hand:
        ascending = True
        count += 1
    else:
        ascending = False
        count += -1
    return count, ascending

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
