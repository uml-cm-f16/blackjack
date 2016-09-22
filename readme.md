# Media Computing Project

## Blackjack Game

### Contributors
josefflores
andrewzlong

### Documentation
uml-cm-f16.github.io/blackjack

### Tasks

Task            | Status | Test | Dependencies      | Note
----------------|--------|------|-------------------|-----
python 3        | Done   | -    | python            | Dependency
pyGame          | Done   | -    | python 3          | Dependency
pyGame research | WIP    | -    | pyGame            |
sphinx          | Done   | -    | python 3          | Dependency
doc generator   | Done   | -    | sphinx            | Extract documentation from code
setup.py        | Done   | -    |                   | Installs and upgrades dependencies
update.py       | Done   | -    |                   | Documents and updates repositories
card class      | Done   | NS   |                   | A playing card.
deck class      | Done   | NS   | card              | A deck of Playing cards.
hand class      | Done   | NS   | card              | A hand of cards.
player class    | WIP    | NS   | hand              | Extends a hand of cards, to make a player.
chips class     | -      | -    | player            | Extends a player by giving them chip handling methods
dealer class    | WIP    | NS   | player, deck      | Extends a player by giving them deck access methods.
blackjack class | WIP    | NS   | dealer            | The blackjack game rules applied to a dealer.
probability     | NS     | NS   | blackjack         | Extends the game by maintaining statistics.
Report          | NS     | All  |                   |
Submission      | NS     | All  |                   |
Demo            | NS     | All  |                   |

### Milestones

#### Part 1 - Simulator 9/21
Write a blackjack simulator. The simulator views the game from a player’s perspective and tries to provide insights to whether to get another card or stop in various scenarios. Assuming that you are the only player, write a blackjack simulator which lists the sum of hands of the player and that of the dealer, whether to get another card, and what the probability of winning when the decision (of getting another card or of declining) is applied.

#### Part 2 - pygame Gui 10/5
Download and install pyGame, and study which features are available in pyGame. 	Submit what the final project will be.

#### Part 3 - Gui
TBD

#### Part 4 - Alpha report 11/2
Submit an interim report on the progress

#### Part 5 - Submision and demo 12/9
TBD

## Coding Standards
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html






