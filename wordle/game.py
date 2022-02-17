import random
from pathlib import Path

from .exceptions import IncompleteWord, InvalidWord

__all__ = ("answers", "allowed_words", "Wordle")


path = Path(__file__).parent

with open(path / "answers.txt", "r", encoding="utf-8") as f:
    answers = f.read().split(",")

with open(path / "allowed_words.txt", "r", encoding="utf-8") as f:
    allowed_words = set(f.read().split(","))
allowed_words.update(answers)


class Wordle:
    MAX_TRIES = 6

    __slots__ = ("word", "characters", "ongoing", "tries")

    def __init__(self) -> None:
        self.word: str = random.choice(answers)
        self.characters: list[str] = []
        self.ongoing: bool = True
        self.tries = 0

    def __repr__(self) -> str:
        characters = "".join(self.characters)
        return f"<Wordle word={self.word!r} characters={characters!r} ongoing={self.ongoing!r}>"

    @property
    def word_length(self) -> int:
        return len(self.word)

    def add_char(self, character: str):
        if not self.can_add_char():
            raise RuntimeError("can't add any more characters")
        self.characters.append(character)

    def can_add_char(self) -> bool:
        return self.ongoing and len(self.characters) < self.word_length

    def submit(self) -> bool:
        if len(self.characters) != self.word_length:
            raise IncompleteWord("".join(self.characters))
        choice = "".join(self.characters)
        if choice == self.word:
            self.ongoing = False
            return True
        if choice not in allowed_words:
            raise InvalidWord(choice)
        self.tries += 1
        self.characters.clear()
        return False
