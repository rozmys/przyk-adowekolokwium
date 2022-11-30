from __future__ import annotations
from court import Court

class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(self,width: float = 68, length: float = 150,
                 address: str = "", year_built: int = 1, name: str = "", common_name: str = "",
                 capacity: int = 0) -> None:
        super().__init__(width, length, address, year_built)
        if capacity < 0:
            self.__capacity = 0
        else:
            self.__capacity = capacity
        self.__name = name
        self.__common_name = common_name

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, value: str) -> None:
        self.name = value

    @property
    def common_name(self) -> str:
        return self.__common_name

    @common_name.setter
    def common_name(self, value: str) -> None:
        self.__common_name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value < 0:
            print("Podana wartość jest nie prawidłowa")

        self.__capacity = value

    def __eq__(self, other: Stadium) -> bool:
        if self.area() == other.area() and self.capacity == other.capacity:
            return True
        return False

    def __ne__(self, other: Stadium) -> bool:
        if self.area() != other.area() or self.capacity != other.capacity:
            return True
        return False

    def __str__(self) -> str:
        if self.common_name == "":
            return f"Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów i szerokości {self.width} metrów." \
                   f"\nPole powierzchni: {self.area()} mkw.\nAdres: {self.address}.\n"\
                   f"Nazwa: {self.name}.\nPojemność stadionu: {self.capacity}."

        return f"Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów i szerokości {self.width} metrów." \
               f"\nPole powierzchni: {self.area()} mkw.\nAdres: {self.address}.\n" \
               f"Nazwa: {self.name}.\n"\
               f"Nazwa zwyczajowa: {self.common_name}.\n"\
               f"Pojemność stadionu: {self.capacity}."
