import pandas as pd
import numpy as np


def create_game():
    try:
        player_count = int(input('How many will be playing today? '))
    except ValueError:
        print('Use a digit for this one!')
        player_count = int(input('How many will be playing today? '))
    players = []
    for i in range(player_count):
        name = input(f'Please enter a name for Player {i + 1}: ')
        players.append(Player(name))

    game = Game(players)
    return game


def score_func(row):
    ba = row.BA
    bid = row.Bid
    result = row.Result
    if ba == 'Yes' and result == bid:
        score_col = bid * 10
    elif ba == 'Yes':
        score_col = bid * -10
    elif result >= bid:
        score_col = bid * 3 + result - bid
    else:
        score_col = bid * -3
    return score_col


class Player:
    def __init__(self, name):
        self.name = name
        self.bids = pd.DataFrame(
            columns=['Round #', 'Card Count', 'Player', 'Bid', 'BA', 'Result'])

    def __repr__(self):
        s = f'{self.name}'
        return s

    def bid(self, round_number, card_count):
        round_data = {
            'Round #': [round_number],
            'Card Count': [card_count],
            'Player': str(self.name),
            'Result': np.NaN
        }
        bid = input(f'What does {self.name} bid? ')
        while not bid.isdigit():
            print('Must enter a digit')
            bid = input('How many will be playing today? ')
        round_data['Bid'] = int(bid)
        if round_data['Bid'] == card_count:
            print('Backalley?')
            round_data['BA'] = str(input())
            if round_data['BA'] in 'YesyesyY':
                round_data['BA'] = 'Yes'
            else:
                round_data['BA'] = 'No'
        else:
            round_data['BA'] = 'No'
        bid_df = pd.DataFrame(round_data)
        self.bids = pd.concat([self.bids, bid_df])
        return bid_df

    def score_round(self):
        result = int(input(f'How many tricks did {self.name} win?'))
        self.bids.fillna(result, inplace=True)
        self.score = self.bids.copy()
        self.score['Score'] = self.score.apply(score_func, axis=1)
        self.score = self.score[['Round #', 'Card Count',
                                 'Player', 'Score']]


class Game():
    def __init__(self):
        player_count = input('How many will be playing today? ')
        while not player_count.isdigit():
            print('Must enter a digit')
            player_count = input('How many will be playing today? ')
        player_count = int(player_count)
        players = []
        for i in range(player_count):
            name = input(f'Please enter a name for Player {i + 1}: ')
            players.append(Player(name))
        self.players = [print(i) for i in players]
        self.max_hand = 54 // len(players)
        if self.max_hand >= 7.0:
            self.max_hand = 7.0
        self.round_number = 1
        self.count = 1
        self.ascending = True

    def card_count(self):
        if self.ascending:
            if self.count < self.max_hand:
                self.count += 1
            else:
                self.count += -1
                self.ascending = False
        else:
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
        scores = scores.sort_values(ascending=False)
        self.players = self.change_order()
        return scores
