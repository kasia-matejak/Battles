# General info
## About the Game
'Battles' is a two players game that gives you the opportunity to get into the role of a sinister wizzard or a knight loyal to the king. Face the powerful, but not always accurate knight's strikes or flawless moderately strong wizzard's magic. Who will triumph in battle? The fate of the kingdom depends on you.

## About the project
For me this project is the introduction to object-oriented and event-driven programming.

## How to Play
Characters are reprezented by the squares on the board:
green square - wizzard
purple square - knight

Each character has keyboard keys assigned to movement:

### Wizzard:
* move up - W
* move down - S
* move left - A
* move right - D 
* attack - Space

### Knight:
* move up - up arrow key
* move down - down arrow key
* move left - left arrow key
* move right - right arrow key
* attack - Enter

Each character has 100 health points.
There is a specified distance, same for each character, that cannot be exceeded in order to attack.
Every wizzard's attempt of attack is successful and causes 10 health points damage.
Half of knight's attempts of attack are successful and they cause 20 health points damage.
The game ends when one of the characters triumphs.

## Technologies
Project is created with:
* python
* pygame

## Setup
Open PowerShell terminal and run:
1. Clone the repository
```sh
git clone https://github.com/kasia-matejak/Battles.git
```
2. Enter the directory
```sh
cd Battles
```
3. Install the required library
```
pip install -r requirements.txt
```
1. Run the game
```
python action.py
```