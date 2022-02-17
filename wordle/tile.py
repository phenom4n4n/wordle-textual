from enum import Enum

import pyfiglet
from rich.align import Align
from rich.panel import Panel
from rich.style import Style
from textual.reactive import Reactive
from textual.widget import Widget

__all__ = ("TileState", "Tile")


class TileState(Enum):
    correct = "correct"
    char_in_word = "char_in_word"
    incorrect = "incorrect"


class Tile(Widget):
    state: Reactive[bool] = Reactive(TileState.incorrect)
    text: Reactive[str] = Reactive("")

    def __init__(self, index: int):
        super().__init__()
        self.index = index

    @property
    def style(self) -> Style:
        if self.state == TileState.correct:
            return Style(bgcolor="#538d4e")
        elif self.state == TileState.char_in_word:
            return Style(bgcolor="#b59f3b")
        border_color = "#565758" if self.text else "#3a3a3c"
        return Style(color=border_color)

    def figlet_text(self) -> str:
        width, height = self.size
        if not self.text:
            return " " * width
        if height < 8:
            font_name = "mini"
        elif height < 10:
            font_name = "small"
        else:
            font_name = "big"
        figlet = pyfiglet.Figlet(font_name, justify="center", width=width)
        return figlet.renderText(self.text)

    def render(self) -> Panel:
        text = self.figlet_text()
        width, height = self.size
        panel = Panel(
            Align.left(text, style="white"), height=height, width=width, style=self.style
        )
        return Align.center(panel, vertical="middle")
