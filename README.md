# Backalley

This is just a project to score a game of Backalley in a Jupyter Notebook. Backalley is similar to Rook, or Up River Down River if you are familiar with those games.

## How to Play & Rules of the Game

Backalley is a betting game. The game begins by dealing each player 1 card and flipping over the top card after every player is dealt their cards. The suit of the top card now flipped over is the trump suit. 

### Betting

Each player, starting with the player left of the dealer, then bids how many tricks they think they will win. In the first round, the most any player can bid is 1 since there is only 1 card to be played. If a player thinks that they will win every trick in the round they have the option to "Backalley" (hence the name of the game). Backalleying comes with a higher reward but also higher consequence when scoring.

### Playing the Round

After the bidding is completed the player with the highest plays the card of their choice. Each player then plays a card and the highest ranking card wins the trick. That player then leads the next trick. This process is repeated until there are no more cards left in the player's hands.<br>
<br>
Some rules for playing a trick are as follows
<ul>
<li>You must play the suit that was lead (first card played) if you have it in your hand</li>
<li>You may never lead with the trump suit until it is the only suit remaining in your hand</li>
<li>The winner of the previous trick plays first</li>
</ul>

#### Order of Card Ranking
<ol>
<li>Colored Joker</li>
<li>Mono Joker</li>
<li>Trump Suit High A --> 2 Low</li>
<li>Lead Suit High A --> 2 Low</li>
<li>Any Other Suit High A --> 2 Low</li>
</ol>
Note: If a card is played that is not trump suit or the suit that was lead, it can *never win* the trick. Take this as an opporunity to get rid of the cards that have a low chance of winning like 2's and 3's!<br>
<br>
Once all the cards are played the round is over, the cards are shuffled and redealt by whoever led the bidding last round but this time with one more card than the previous round. The game is played like this up until the maximum number of cards each player can have, and then goes back down. For example with 6 people the game would go from one card up to seven cards, then back down to one card.

### Scoring

After the round is over the scores are recorded. Scoring is all or nothing. Each trick a player bids is worth 3 points and every trick over a players bid is worth 1 point.  
If a player bids two tricks and wins 2 tricks they receive 6 points, (3 points/trick * 2 tricks bid).  
If a player bids 2 tricks and wins 3 they receive 7 points, (3 points/trick * 2 tricks bid) + (1 point/additional trick * 1 additional trick).  
If a player bids 3 tricks and wins anything less than 3 they receive -9 points, (-3 points/trick * 2 tricks bid).  
<br>
When a player backalleys the worth of a trick increases to 10 points. Meaning,  
If a player backalleys with 2 cards and wins they receive 20 points, (10 points/trick * 2 tricks bid).  
If a player backalleys with 2 cards and do not win all 2 tricks they receive -20 points, (-10 points/trick * 2 tricks bid).  
<br>
Note: The 1 point per additional bid will never come into effect when backalleying since the player is betting they will win every trick.
<br>
<br>
I hope that you enjoy playing this game as much as I do!
