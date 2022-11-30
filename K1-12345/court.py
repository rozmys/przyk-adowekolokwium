from __future__ import annotations
import datetime

class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68, length: float = 150,
                 address: str = "", year_built: int = 1) -> None:
        if 90 <= length <= 120 and 45 <= width <= 90:
            self.__length = length
            self.__width = width
        else:
            self.__length = 150
            self.__width = 68
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        if 45 <= value <= 90:
            self.__width = value

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float) -> None:
        if 90 <= value <= 120:
            self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.setter
    def year_built(self, value: int) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.__length * self.__width

    @staticmethod
    def validate(arg: Court) -> None:
        year = datetime.datetime.year
        if arg.year_built > year and arg.year_built < 0:
            arg.year_built = year

    def __str__(self) -> str:
        return f"Boisko wybudowane w roku {self.__year_built}, o długości {self.__length} metrów i szerokości {self.__width} metrów." \
               f"\nPole powierzchni: {self.area()} mkw.\nAdres: {self.__address}"


