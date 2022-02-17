__all__ = ("WordleException", "InvalidWord")


class WordleException(Exception):
    """
    Base class for exceptions.
    """


class IncompleteWord(WordleException):
    """
    Raised when a word is incomplete.
    """

    def __init__(self, word: str) -> None:
        self.word = word
        super().__init__("Not enough letters")


class InvalidWord(WordleException):
    """
    Raised when a submited word is not valid.
    """

    def __init__(self, word: str) -> None:
        self.word = word
        super().__init__("Not in word list")
