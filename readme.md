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

  `python ./setup.py install`

+ Run unit tests

  `python ./setup.py test`

+ Run application.

  `python ./main.py`

+ Update application: `$message` is the git commit message to use.

  `python ./setup.py save "$message"`

### Tasks

Task            | Status | Unit Test | Usability Test | Owner  | Dependencies      | Note
----------------|--------|-----------|----------------|--------|-------------------|---------------
python 3        | D      | -         | -              | All    | -                 | Dependency.
pyGame          | D      | -         | -              | All    |  python 3         | Dependency.
pyGame research | D      | -         | -              | Andrew |  pyGame           | Learn about to pyGame.
setup.py        | D      | -         | D              | Jose   |  -                | Installs and upgrades dependencies.
card class      | D      | D         | -              | Jose   |  -                | A playing card.
deck class      | D      | D         | -              | Jose   |  card             | A deck of Playing cards.
hand class      | D      | D         | -              | Jose   |  card             | A hand of cards.
player class    | D      | D         | -              | Jose   |  hand             | Extends a hand of cards, to make a player.
dealer class    | D      | D         | -              | Jose   |  player, deck     | Extends a player by giving them deck access methods.
blackjack class | D      | D         | -              | Jose   |  dealer, player   | The blackjack game rules applied to a dealer.
engine          | D      | -         | D              | All    |  blackjack        | -
Report          | W      | -         | -              | All    |  -                | -
Submission      | W      | -         | -              | All    |  -                | -
Demo            | W      | -         | -              | All    |  -                | -

### Milestones
Date  | Item | Description
------|------|------------
09/23 | Simulator | Write a blackjack simulator. The simulator views the game from a player’s perspective and tries to provide insights to whether to get another card or stop in various scenarios. Assuming that you are the only player, write a blackjack simulator which lists the sum of hands of the player and that of the dealer, whether to get another card, and what the probability of winning when the decision (of getting another card or of declining) is applied.
10/05 | pyGame Gui | Download and install pyGame, and study which features are available in pyGame. Submit what the final project will be.
12/09 | Report | Submit a report on the progress
12/09 | Submission | Final submission and demo.

## Coding Standards
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html






