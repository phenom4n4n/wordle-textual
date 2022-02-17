# Wordle, playable from the CLI
<h1 align="center">
  <img src="https://imgur.com/6IRuC8A.png"></a>
</h1>

This project seeks to emulate Wordle in your shell, using [Textual](https://github.com/Textualize/textual).
This project uses the "official" answers and allowed words lists found in Wordle's source code, but the answer is randomized every time you play the game.

Currently, only the basic functionality of the game is implemented, and various elements are missing, such as the win screen and error popups.

# Prerequsities
- [Python 3.10 or higher](https://www.python.org/downloads/)

# Installation
Clone this repository and CD to its root directory:
```
git clone https://github.com/phenom4n4n/wordle-textual
cd wordle-textual
```
Create a new Python virtual environment:
```
python -m venv .venv
```
Activate the virtual environment:

**Unix**
```
source .venv/bin/activate
```
**Windows**
```
.venv\Scripts\activate
```
And install the requirements
```
pip install -Ur requirements.txt
```

# Playing the game
After CD'ing to the root directory and activating the virtual environment as shown above, run the game with Python:
```
python main.py
```

# Credits
- Will McGugan, who maintains [Textual](https://github.com/Textualize/textual) and [Rich](https://github.com/Textualize/rich), the core Python libraries for the game's TUI
