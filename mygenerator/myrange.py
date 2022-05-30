from typing import Union

from .myiterator import MyIterator


class MyRange:

    def __init__(self, start: Union[int, float], end: Union[int, float], step: Union[int, float] = 1) -> None:

        self._check_types(start=start, end=end, step=step)

        self.start = start
        self.end = end
        self.step = step

        self.set_number_of_decimals()

        self.range_lenght = int(abs((self.end - self.start) / self.step))

    def set_number_of_decimals(self) -> None:
        max_number_of_decimal = 0
        for number in (self.start, self.end, self.step): # Get max decimal number from arguments
            if isinstance(number, int):
                continue

            number_of_decimal = len(str(number).split('.')[-1])
            max_number_of_decimal = max(max_number_of_decimal, number_of_decimal)

        self.number_of_decimals = max_number_of_decimal

    def to_string(self) -> str:
        return " ".join([str(i) for i in self])

    def __iter__(self) -> MyIterator:
        return MyIterator(self.start, self.end, self.step, self.number_of_decimals)

    def __getitem__(self, index: int) -> Union[int, float]:
        if not isinstance(index, int):
            raise TypeError(f"index must be 'int', got '{index.__class__.__name__}' instead")

        if not (0 <= abs(index) < len(self)) and (index != -len(self)):
            raise IndexError(f"Index {index} is out of range.")

        if index >= 0:
            value = round(self.start + index * self.step, self.number_of_decimals)
        else:
            value = round(self.end + index * self.step, self.number_of_decimals)

        return value

    def __in__(self, value) -> bool:
        if self.start <= value < self.end:
            val = round(value - self.start, self.number_of_decimals)
            return val % self.step == 0

        return False

    def __min__(self) -> Union[int, float]:
        return min(self[0], self[-1])

    def __max__(self) -> Union[int, float]:
        return max(self[0], self[-1])

    def __len__(self) -> int:
        return self.range_lenght

    def __sum__(self) -> Union[int, float]:
        return len(self) * (self.start + self.end) / 2 

    @staticmethod
    def _check_types(**kwargs) -> None:

        if kwargs['step'] == 0:
            raise ValueError("step argument can not be 0.")

        for key, value in kwargs.items():
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(f"{key} argument must be 'int' or 'float', got '{value.__class__.__name__}' instead.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(start={self.start}, end={self.end}, step={self.step})"
    