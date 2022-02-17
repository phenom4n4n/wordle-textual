import string
from typing import Iterable

from textual import events
from textual.app import App
from textual.widgets import Header

from .exceptions import WordleException
from .game import Wordle
from .tile import Tile, TileState


class WordleApp(App):
    def __init__(self, **kwargs):
        kwargs["title"] = "Wordle"
        super().__init__(**kwargs)
        self.game = Wordle()

    async def on_mount(self):
        await self.view.dock(Header(style="bold white on black", clock=False), edge="top")
        grid = await self.view.dock_grid(edge="bottom", name="grid")
        for x in range(self.game.word_length):
            grid.add_column(fraction=1, name=str(x))
        for y in range(self.game.MAX_TRIES):
            grid.add_row(fraction=1, name=str(y))
        grid.set_repeat(True, True)
        tiles = (Tile(i) for i in range(30))
        grid.place(*tiles)

    def tiles(self, *, filled: bool = None, reverse: bool = False) -> Iterable[Tile]:
        grid = self.view.named_widgets["grid"]
        tiles = grid.layout.get_widgets()
        if reverse:
            tiles = reversed(tiles)
        if filled is not None:
            check = lambda tile: bool(tile.text) is filled
            tiles = filter(check, tiles)
        return tiles

    def tiles_from_row(self, row: int) -> Iterable[Tile]:
        return filter(lambda tile: tile.index // 5 == row, self.tiles())

    async def on_key(self, event: events.Key):
        key = event.key
        if key in string.ascii_letters:
            self.add_char(key)
            return

        if key == "enter":
            try:
                correct = self.game.submit()
            except WordleException as error:
                await self.display_error(error)
            else:
                if correct:
                    for tile in self.tiles_from_row(self.game.tries):
                        tile.state = TileState.correct
                else:
                    for i, tile in enumerate(self.tiles_from_row(self.game.tries - 1)):
                        char = tile.text.lower()
                        if char == self.game.word[i]:
                            tile.state = TileState.correct
                        elif char in self.game.word:
                            tile.state = TileState.char_in_word
        elif key == "ctrl+h":
            if self.game.characters:
                self.game.characters.pop()
                tile: Tile = next(self.tiles(filled=True, reverse=True))
                tile.text = ""

    def add_char(self, char: str):
        if not self.game.can_add_char():
            return
        self.game.add_char(char)
        tile: Tile = next(self.tiles(filled=False))
        tile.text = char.upper()

    async def display_error(self, error: WordleException):
        print(error)
