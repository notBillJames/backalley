import pandas as pd 
import numpy as np 

def score_func(row):
    if row.BA == 'y' and row.Result == row.Bid:
      row['Score'] = 10 * row.Bid 
    elif row.BA == 'y':
      row['Score'] = -10 * row['Bid']
    elif row.Bid >= row.Result:
      row['Score'] = 3 * row['Bid'] + row['Result'] % row['Bid']
    else:
      row['Score'] = -3 * row['Bid']

class Player():
  def __init__(self, name):
    self.name = name
    self.bids = pd.DataFrame(columns=['Round #', 'Card Count', 'Player', 'Bid', 'BA'])
  
  def bid(self, round_number, card_count):
    round_data = {
      'Round #': [round_number],
      'Card Count': [card_count],
      'Player': str(self.name),
      'Result': np.NaN,
      'Score': np.NaN
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
    score_df = self.bids.copy()
    print(f'What did {self.name} get?')
    result = int(input())
    result = {
      "Round #": score_df['Round #'].max(),
      "Result": result
    }
    result = pd.DataFrame.from_dict(result)
    result.set_index('Round #')
    score_df = score_df.update(result)
    score_df['Score'] = score_df.apply(score_func, axis=1)


    