from enum import Enum


class NaturalRUCLetter(Enum):
    NO_LETTER = ("", "00", "00", "No letter")
    E = ("E", "5", "66", "Foreigner")
    PE = ("PE", "75", "82", "Panamanian Foreigner ")
    N = ("N", "4", "92", "Naturalized")
    AV = ("AV", "15", "9595", "Before the system")
    PI = ("PI", "79", "9595", "Indigenous People")

    def __init__(self, letter, code, validation_code, name):
        self.letter = letter
        self.code = code
        self.validation_code = validation_code
        self.code_name = name

    @classmethod
    def from_code(cls, letter: str):
        for member in cls:
            if member.letter == letter.upper():
                return member
        raise ValueError(f"Invalid RUC letter: {letter}")
