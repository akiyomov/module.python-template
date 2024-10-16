from ._base import MyBase


class StripText(MyBase):
    def __init__(self, text: str = "text"):
        super().__init__(text)
        self.text = text

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        if not isinstance(text, str):
            raise TypeError("`text` must be a string!")
        text = text.strip()
        if text == "":
            raise ValueError("`text` cannot be an empty string after stripping!")
        self.__text = text
