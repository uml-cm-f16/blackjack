# Media Computing Project

## Blackjack Game

### Contributors

Contributor | Username
------------|------------
Jose Flores | josefflores
Andrew Long | andrewzlong

### Documentation
Our documentation can be found in [uml-cm-f16.github.io/blackjack/](https://uml-cm-f16.github.io/blackjack/).

### Run commands

+ Install Dependencies.

  `python ./setup.py`

+ Run application.

  `python ./main.py`

+ Update application: `$message` is the git commit message to use.

  `python update.py "$message"`

### Tasks

Task            | Status | Test | Dependencies      | Note
----------------|--------|------|-------------------|-----
python 3        | Done   | -    | -                 | Dependency.
pyGame          | Done   | -    | python 3          | Dependency.
pyGame research | WIP    | -    | pyGame            | Learn about to pyGame.
sphinx          | Done   | -    | python 3          | Dependency
doc generator   | Done   | -    | sphinx            | Extract documentation from code.
setup.py        | Done   | -    | -                 | Installs and upgrades dependencies.
update.py       | Done   | -    | -                 | Documents and updates repositories.
card class      | Done   | NS   | -                 | A playing card.
deck class      | Done   | NS   | card              | A deck of Playing cards.
hand class      | Done   | NS   | card              | A hand of cards.
player class    | WIP    | NS   | hand              | Extends a hand of cards, to make a player.
chips class     | -      | -    | player            | Extends a player by giving them chip handling methods.
dealer class    | WIP    | NS   | player, deck      | Extends a player by giving them deck access methods.
blackjack class | WIP    | NS   | dealer            | The blackjack game rules applied to a dealer.
probability     | NS     | NS   | blackjack         | Extends the game by maintaining statistics.
Report          | NS     | All  | -                 | -
Submission      | NS     | All  | -                 | -
Demo            | NS     | All  | -                 | -

### Milestones
Date  | Item | Description
------|------|------------
09/23 | Simulator | Write a blackjack simulator. The simulator views the game from a player’s perspective and tries to provide insights to whether to get another card or stop in various scenarios. Assuming that you are the only player, write a blackjack simulator which lists the sum of hands of the player and that of the dealer, whether to get another card, and what the probability of winning when the decision (of getting another card or of declining) is applied.
10/05 | pyGame Gui | Download and install pyGame, and study which features are available in pyGame. Submit what the final project will be.
10/20 | Gui-Sim integration | TBD
11/02 | Alpha report | Submit an interim report on the progress
12/09 | Submission | Final submission and demo.

## Coding Standards
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html






